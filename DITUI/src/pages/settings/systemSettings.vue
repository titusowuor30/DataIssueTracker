<template>
  <VApp>
    <VMain>
      <VContainer>
        <VDataTable
          :headers="headers"
          :items="data"
          :items-per-page="perPage"
          :total-items="totalItems"
          :loading="loading"
          @page-count="fetchData"
        >
          <template #top>
            <VRow>
              <VCol>
                <VTextField
                  v-model="search"
                  append-icon="mdi-magnify"
                  label="Search"
                  single-line
                  hide-details
                />
              </VCol>
            </VRow>
          </template>
          <template #item.action_taken="{ item }">
            <VChip
              :color="getChipColor(item.action_taken)"
              dark
            >
              {{ item.action_taken }}
            </VChip>
          </template>
        </VDataTable>
      </VContainer>
    </VMain>
  </VApp>
</template>

<script setup>
import { ref, watch } from 'vue'

const headers = ref([
  { text: 'Patient ID', value: 'patient_id' },
  { text: 'Date of Entry', value: 'date_of_entry' },
  { text: 'Inconsistency', value: 'inconsistency' },
  { text: 'Action Taken', value: 'action_taken' },
])

const data = ref([])
const perPage = ref(10)
const totalItems = ref(0)
const currentPage = ref(1)
const loading = ref(false)
const search = ref('')

const fetchData = () => {
  // Fetch data from your Django REST API based on currentPage, perPage, and search
  // Update data and totalItems with the fetched data
  // Use Axios or fetch API to make the HTTP request

  axios
    .get('http://127.0.0.1:8000/api/data_issues/', {
      params: {
        limit: perPage.value,
        offset: (currentPage.value - 1) * perPage.value,
        search: search.value,
      },
    })
    .then(response => {
      data.value = response.data.results
      totalItems.value = response.data.count
    })
    .catch(error => {
      console.error('Error fetching data:', error)
    })
}

const getChipColor = action => {
  // Define colors based on the action taken
  // You can customize this based on your requirements
  switch (action) {
  case 'Pending':
    return 'orange'
  case 'Completed':
    return 'green'
  default:
    return 'grey'
  }
}

watch(currentPage, fetchData)
watch(perPage, fetchData)
watch(search, fetchData)

onMounted(() => {
  fetchData()
})
</script>
