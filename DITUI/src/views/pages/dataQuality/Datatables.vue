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

      <table class="data-issues-table">
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
            <th>Country</th>
            <th>Facility</th>
            <th>Patient ID</th>
            <th>Date of Entry</th>
            <th>Inconsistency</th>
            <th>Action Taken</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="issue in filteredDataIssues"
            :key="issue.id"
          >
            <td>
              <input
                v-model="selectedRows"
                type="checkbox"
                :value="issue.id"
              >
            </td>
            <td>{{ issue.id }}</td>
            <td>{{ issue.country }}</td>
            <td>{{ issue.facility_name }}</td>
            <td>{{ issue.patient_id }}</td>
            <td>{{ issue.date_of_entry }}</td>
            <td>{{ issue.inconsistency }}</td>
            <td>{{ issue.action_taken }}</td>
          </tr>
        </tbody>
      </table>
      <p
        v-if="filteredDataIssues.length === 0"
        class="text-muted px-2"
      >
        No data found!
      </p>
      <VCard class="px-2 py-2">
        <VRow>
          <VCol cols="3">
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
              color="primary"
              class="px-2 py-2"
              outlined
              @click="updateDataIssues"
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

const currentPage = ref(1)
const perPage = ref(10) // Adjust as needed
const totalItems = ref(0)
const dataIssues = ref([])
const action = ref("Pending")

//reports
const exportData = ref([])

const rptheaders = [
  "ID",
  "Country",
  "Facility",
  "Patient ID",
  "Date of Entry",
  "Inconsistency",
  "Action Taken",
]

const exportcsvFileName = ref("data_issues.csv")

const actions = reactive([
  "Entry Corrected",
  "Data Matches Source Document",
  "Data Already Available",
  "No Data Needed",
  "Pending",
])

const perPageOptions = reactive([1, 5, 10, 20, 50, 100, 500, 100])

const apiUrl = "data_issues"

// Filters
const searchText = ref("")
const filteredDataIssues = ref([])
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
        limit: perPage.value,
        offset: (currentPage.value - 1) * perPage.value,
      },
    })
    .then(response => {
      dataIssues.value = response.data.results
      totalItems.value = response.data.count
      exportData.value = dataIssues.value.map(issue => [
        issue.id,
        issue.country,
        issue.facility_name,
        issue.patient_id,
        issue.date_of_entry,
        issue.inconsistency,
        issue.action_taken,
      ]) //map data as a list
      exportData.value.unshift(rptheaders) //add headers as first row
      console.log(exportData.value)
      applyFilters()
    })
    .catch(error => {
      console.error("Error loading data:", error)
    })
}

const applyFilters = () => {
  filteredDataIssues.value = dataIssues.value.filter(issue => {
    const searchTextLower = searchText.value.toLowerCase()

    return (
      issue.patient_id.toLowerCase().includes(searchTextLower) ||
      issue.date_of_entry.includes(searchTextLower) ||
      issue.inconsistency.toLowerCase().includes(searchTextLower) ||
      issue.action_taken.toLowerCase().includes(searchTextLower)
    )
  })
}

const selectAllRows = () => {
  if (selectAll.value) {
    selectedRows.value = filteredDataIssues.value.map(issue => issue.id)
  } else {
    selectedRows.value = []
  }
}

watch(selectedRows, () => {
  selectAll.value = selectedRows.value.length === filteredDataIssues.value.length
})

const handleCSVExport = ({ filename, data }) => {
  console.log("Exporting to CSV:", filename, data)
  exportCSV(data, filename)
}

const exportPDF = () => {
  // Add code to export data to PDF
}

const updateDataIssues = () => {
  if (selectedRows.value.length === 0) {
    return Swal.fire("No data to process!", "Please select at least one issue!", "info")
  } else if (selectedRows.value.length === 1) {
    updateSingele()
  } else {
    performBulkAction()
  }
}

const updateSingele = () => {
  const data_id = selectedRows.value[0]

  const data = {
    action: action.value,
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
    .put("data_issues/" + data_id + "/", data)
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
    action: action.value,
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
    .post("data_issues/", data)
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
  setInterval(loadData, 10000)
})
onUnmounted(() => {
  clearInterval(loadData)
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
