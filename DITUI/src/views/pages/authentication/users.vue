<template>
  <div>
    <VCard>
      <VCardTitle>
        <VRow
          style="
            background:
              linear-gradient(
                90deg,
                rgb(246, 235, 255) 0%,
                rgb(240, 225, 225) 50%,
                rgb(240, 239, 237) 100%
              );
"
          align="center"
          justify="space-between"
          class="px-2 m-0"
        >
          <VCol cols="3">
            <VTextField
              v-model="searchText"
              placeholder="Search Patient ID, Date, or Status"
              label="Search"
              outlined
              dense
              @input="applyFilters"
            />
          </VCol>
          <VCol cols="3">
            <div class="select-per-page">
              <VSelect
                v-model="perPage"
                :items="perPageOptions"
                label="Records Per Page"
                @click="loadData"
              />
            </div>
          </VCol>
          <VCol cols="4" class="text-right">
            <CSVExport
              :filename="exportcsvFileName"
              :data="exportData"
              @export-csv="handleCSVExport"
            />

            <VIcon size="40" icon="bxs-file-pdf" class="text-error" />
          </VCol>
        </VRow>
      </VCardTitle>

      <table class="data-issues-table">
        <thead>
          <tr>
            <th>
              <input v-model="selectAll" type="checkbox" @change="selectAllRows" />
            </th>
            <th>ID</th>
            <th>Username</th>
            <th>Email</th>
            <th>Role</th>
            <th>Gender</th>
            <th>Phone</th>
            <th>Address</th>
            <th>Organisation</th>
            <th>Country</th>
            <th>State</th>
            <th>ZIP</th>
            <th>Timezone</th>
            <th>Facilities</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="user in filteredUsers"
            :key="user.id"
            @click="getUserDetails(user.id)"
          >
            <td>
              <input v-model="selectedRows" type="checkbox" :value="user.id" />
            </td>
            <td>{{ user.id }}</td>
            <td>{{ user.username }}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.role.role_name }}</td>
            <td>{{ user.gender }}</td>
            <td>{{ user.phone }}</td>
            <td>{{ user.address }}</td>
            <td>{{ user.organisation }}</td>
            <td>{{ user.country }}</td>
            <td>{{ user.state }}</td>
            <td>{{ user.zip }}</td>
            <td>{{ user.timezone }}</td>
            <td>{{ user.facilities.map((f) => f.facility_code).join(", ") }}</td>
          </tr>
        </tbody>
      </table>
      <p v-if="filteredUsers.length === 0" class="text-muted px-2">No data found!</p>
      <VCard class="px-2 py-2">
        <VRow>
          <VCol cols="3">
            <div class="select-action">
              <VSelect v-model="action" :items="actions" label="Select Action" />
            </div>
          </VCol>
          <VCol cols="3">
            <VBtn color="primary" class="px-2 py-2" outlined @click="updateUser">
              <span v-if="selectedRows.length > 1">Apply Bulk Action</span>
              <span v-else>Apply Action</span>
            </VBtn>
          </VCol>
        </VRow>
      </VCard>
    </VCard>

    <div class="pagination">
      <VPagination
        v-model="currentPage"
        :length="Math.ceil(totalItems / perPage)"
        @click="loadData"
      />
    </div>
  </div>
</template>

<script setup>
import axios from "@/axiosConfig";
import { exportCSV } from "@/components/report/exportUtils";
import CSVExport from "@/pages/report/CSVExport.vue";
import Swal from "sweetalert2";
import { onMounted, reactive, ref, watch } from "vue";

const currentPage = ref(1);
const perPage = ref(10); // Adjust as needed
const totalItems = ref(0);
const users = ref([]);
const action = ref("Pending");

//reports
const exportData = ref([]);

const rptheaders = [
  "ID",
  "Username",
  "Email",
  "Role",
  "Gender",
  "Phone",
  "Address",
  "Organisation",
  "Country",
  "State",
  "ZIP",
  "Timezone",
  "Facilities",
];

const exportcsvFileName = ref("users.csv");

const actions = reactive(["Disable", "Suspend"]);

const perPageOptions = reactive([1, 5, 10, 20, 50, 100, 500, 100]);

const apiUrl = "usersapi";

// Filters
const searchText = ref("");
const filteredUsers = ref([]);
const selectedRows = ref([]);
const selectAll = ref(false);

const updatePage = (page) => {
  currentPage.value = page;
  loadData();
};

const loadData = () => {
  axios
    .get(apiUrl, {
      params: {
        limit: perPage.value,
        offset: (currentPage.value - 1) * perPage.value,
      },
    })
    .then((response) => {
      users.value = response.data.results;
      totalItems.value = response.data.count;
      exportData.value = users.value.map((user) => [
        user.id,
        user.username,
        user.email,
        user.role.role_name,
        user.gender,
        user.phone,
        user.address,
        user.organisation,
        user.country,
        user.state,
        user.zip,
        user.timezone,
        JSON.stringify(user.facilities.map((f) => f.facility_code).join(",")).toString(),
      ]); //map data as a list
      exportData.value.unshift(rptheaders); //add headers as first row
      console.log(exportData.value);
      applyFilters();
    })
    .catch((error) => {
      console.error("Error loading data:", error);
    });
};

const applyFilters = () => {
  filteredUsers.value = users.value.filter((user) => {
    const searchTextLower = searchText.value.toLowerCase();
    return (
      user.username.toLowerCase().includes(searchTextLower) ||
      user.email.includes(searchTextLower) ||
      user.country.toLowerCase().includes(searchTextLower)
    );
  });
};

const selectAllRows = () => {
  if (selectAll.value) {
    selectedRows.value = filteredUsers.value.map((user) => user.id);
  } else {
    selectedRows.value = [];
  }
};

watch(selectedRows, () => {
  selectAll.value = selectedRows.value.length === filteredUsers.value.length;
});

const handleCSVExport = ({ filename, data }) => {
  console.log("Exporting to CSV:", filename, data);
  exportCSV(data, filename);
};

const exportPDF = () => {
  // Add code to export data to PDF
};

const updateUser = () => {
  if (selectedRows.value.length === 0) {
    return Swal.fire("No data to process!", "Please select at least one issue!", "info");
  } else if (selectedRows.value.length === 1) {
    updateSingele();
  } else {
    performBulkAction();
  }
};

const updateSingele = () => {
  const data_id = selectedRows.value[0];

  const data = {
    action: action.value,
  };

  Swal.fire({
    icon: "info",
    title: "Please Wait!",
    html: "Processing...", // add html attribute if you want or remove
    allowOutsideClick: false,
    showConfirmButton: false,
    willOpen: () => {
      Swal.showLoading();
    },
  });
  axios
    .put("data_issues/" + data_id + "/", data)
    .then((response) => {
      console.log(response);
      Swal.fire({
        icon: "success",
        title: "success!",
        html: "Process completed successfully",
        timer: 3000,
      }).finally(() => {
        Swal.close();
      });
      selectedRows.value = [];
      loadData();
    })
    .catch((error) => {
      console.error("Error loading data:", error);
      Swal.fire("Error!", "Something went wrong:" + error, "error");
    });
};

const performBulkAction = () => {
  const data = {
    data_ids: selectedRows.value,
    action: action.value,
  };

  Swal.fire({
    icon: "info",
    title: "Please Wait!",
    html: "Processing...", // add html attribute if you want or remove
    allowOutsideClick: false,
    showConfirmButton: false,
    willOpen: () => {
      Swal.showLoading();
    },
  });
  axios
    .post("data_issues/", data)
    .then((response) => {
      console.log(response);
      Swal.fire({
        icon: "success",
        title: "success!",
        html: "Bulk update process completed successfully!",
        timer: 3000,
      }).finally(() => {
        Swal.close();
      });
      selectedRows.value = [];
      loadData();
    })
    .catch((error) => {
      console.error("Error loading data:", error);
      Swal.fire("Error!", "Something went wrong:" + error, "error");
    });
};

onMounted(() => {
  loadData();
});
</script>

<style scoped>
/* Add your table styles here */
.filters {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-block-end: 16px;
}

.filters .search input {
  padding: 8px;
  inline-size: 300px;
}

.filters .export-buttons button {
  border: none;
  background-color: #4caf50;
  color: white;
  cursor: pointer;
  padding-block: 8px;
  padding-inline: 16px;
}

.filters .export-buttons button + button {
  margin-inline-start: 10px;
}

.data-issues-table {
  border-collapse: collapse;
  inline-size: 100%;
}

.data-issues-table th,
.data-issues-table td {
  padding: 8px;
  border: 1px solid #ddd;
  text-align: start;
}

.data-issues-table th {
  background-color: #f2f2f2;
}

.pagination {
  margin-block-start: 20px;
  text-align: center;
}

.pagination button {
  border: none;
  background-color: #4caf50;
  color: white;
  cursor: pointer;
  padding-block: 8px;
  padding-inline: 16px;
}

.pagination button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
