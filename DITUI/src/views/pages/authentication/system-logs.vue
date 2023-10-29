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
          <VCol cols="2">
            <div class="select-per-page">
              <VSelect
                v-model="perPage"
                :items="perPageOptions"
                label="Records Per Page"
                @click="loadData"
              />
            </div>
          </VCol>
          <VCol
            cols="4"
            class="text-right"
          >
            <CSVExport
              :filename="exportcsvFileName"
              :data="exportData"
              @export-csv="handleCSVExport"
            />

            <VIcon
              size="40"
              icon="bxs-file-pdf"
              class="text-error"
            />
          </VCol>
        </VRow>
      </VCardTitle>

      <table class="data-logs-table">
        <thead>
          <tr>
            <th>
              <input
                v-model="selectAll"
                type="checkbox"
                @change="selectAllRows"
              >
            </th>
            <th>ID</th>
            <th>User</th>
            <th>Timestamp</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="log in filtereduserlogs"
            :key="log.id"
          >
            <td>
              <input
                v-model="selectedRows"
                type="checkbox"
                :value="log.id"
              >
            </td>
            <td>{{ log.id }}</td>
            <td>{{ log.user.email }}</td>
            <td>{{ log.timestamp }}</td>
            <td>{{ log.action }}</td>
          </tr>
        </tbody>
      </table>
      <p
        v-if="filtereduserlogs.length === 0"
        class="text-muted px-2"
      >
        No data found!
      </p>
      <VCard class="px-2 py-2">
        <VRow>
          <VCol 
            v-if="isAdmin" 
            cols="3"
          >
            <div class="select-action">
              <VSelect
                v-model="action"
                :items="actions"
                label="Select Action"
              />
            </div>
          </VCol>
          <VCol cols="3">
            <VBtn
              v-if="isAdmin"
              color="primary"
              class="px-2 py-2"
              outlined
              @click="updateuserlogs"
            >
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
import axios from "@/axiosConfig"
import { exportCSV } from "@/components/report/exportUtils"
import CSVExport from "@/pages/report/CSVExport.vue"
import Swal from "sweetalert2"
import { onMounted, reactive, ref, watch } from "vue"
import { useStore } from "vuex"

const store = useStore()
const currentPage = ref(1)
const perPage = ref(10) // Adjust as needed
const totalItems = ref(0)
const userlogs = ref([])
const user = ref(store.state.auth.user)
const isAdmin=ref(JSON.parse(localStorage.getItem("isAdmin")))
const action = ref("Delete")

//reports
const exportData = ref([])

const rptheaders = [
  "ID",
  "User",
  "Timestamp",
  "Action",
]

const exportcsvFileName = ref(`${user.value.username}_logs.csv`)

const actions = reactive([
  "Delete",
])

const perPageOptions = reactive([1, 5, 10, 20, 50, 100, 500, 1000, 1500, 2000])

const apiUrl = "user-logs/"

// Filters
const searchText = ref("")
const timestamp = ref()
const filtereduserlogs = ref([])
const selectedRows = ref([])
const selectAll = ref(false)


const updatePage = page => {
  currentPage.value = page
  loadData()
}

const loadData = () => {
  axios
    .get(apiUrl, {
      params: {
        action: searchText.value,
        timestamp: timestamp.value,
        limit: perPage.value,
        offset: (currentPage.value - 1) * perPage.value,
      },
    })
    .then(response => {
      userlogs.value = response.data.results
      totalItems.value = response.data.count
      exportData.value = userlogs.value.map(log => [
        log.id,
        log.user.email,
        log.timestamp,
        log.action,
      ]) //map data as a list
      exportData.value.unshift(rptheaders) //add headers as first row
      applyFilters()
    })
    .catch(error => {
      console.error("Error loading data:", error)
    })
}

const applyFilters = () => {
  filtereduserlogs.value = userlogs.value.filter(log => {
    const searchTextLower = searchText.value.toLowerCase()

    return (
      log.id.toString().includes(searchTextLower) ||
      log.action.includes(searchTextLower) ||
      log.timestamp.toString().includes(searchTextLower) ||
      log.user.email.toLowerCase().includes(searchTextLower)
    )
  })
}

const selectAllRows = () => {
  selectedRows.value = selectAll.value ? filtereduserlogs.value.map(log => log.id) : []
}

watch(selectedRows, () => {
  selectAll.value = selectedRows.value.length === filtereduserlogs.value.length
})

const handleCSVExport = ({ filename, data }) => {
  console.log("Exporting to CSV:", filename, data)
  exportCSV(data, filename)
}

const exportPDF = () => {
  // Add code to export data to PDF
}

const updateuserlogs = () => {
  if (selectedRows.value.length === 0) {
    return Swal.fire("No data to process!", "Please select at least one log!", "info")
  } else if (selectedRows.value.length === 1) {
    updateSingele()
  } else {
    performBulkAction()
  }
}

const updateSingele = () => {
  const data_id = selectedRows.value[0]

  const data = {
    command: action.value,
  }

  Swal.fire({
    icon: "info",
    title: "Please Wait!",
    html: "Processing...", // add html attribute if you want or remove
    allowOutsideClick: false,
    showConfirmButton: false,
    willOpen: () => {
      Swal.showLoading()
    },
  })
  axios
    .delete("user-logs/" + data_id + "/")
    .then(response => {
      console.log(response)
      Swal.fire({
        icon: "success",
        title: "success!",
        html: "Process completed successfully",
        timer: 3000,
      }).finally(() => {
        Swal.close()
      })
      selectedRows.value = []
      loadData()
    })
    .catch(error => {
      console.error("Error loading data:", error)
      Swal.fire("Error!", "Something went wrong:" + error, "error")
    })
}

const performBulkAction = () => {
  const data = {
    data_ids: selectedRows.value,
    command: action.value,
  }

  Swal.fire({
    icon: "info",
    title: "Please Wait!",
    html: "Processing...", // add html attribute if you want or remove
    allowOutsideClick: false,
    showConfirmButton: false,
    willOpen: () => {
      Swal.showLoading()
    },
  })
  axios
    .post("user-logs/", data)
    .then(response => {
      console.log(response)
      Swal.fire({
        icon: "success",
        title: "success!",
        html: "Bulk update process completed successfully!",
        timer: 3000,
      }).finally(() => {
        Swal.close()
      })
      selectedRows.value = []
      loadData()
    })
    .catch(error => {
      console.error("Error loading data:", error)
      Swal.fire("Error!", "Something went wrong:" + error, "error")
    })
}

onMounted(() => {
  loadData()
})
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

.data-logs-table {
  border-collapse: collapse;
  inline-size: 100%;
}

.data-logs-table th,
.data-logs-table td {
  padding: 8px;
  border: 1px solid #ddd;
  text-align: start;
}

.data-logs-table th {
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
