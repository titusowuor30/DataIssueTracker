<script setup>
import axios from '@/axiosConfig'

const data = ref([])
const perPage = ref(10)
const totalItems = ref(0)
const currentPage = ref(1)
const loading = ref(false)
const search = ref('')

const fetchData = () => {
  axios
    .get('data_issues/', {
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

watch(currentPage, fetchData)
watch(perPage, fetchData)
watch(search, fetchData)

onMounted(() => {
  fetchData()
})
</script>

<template>
  <VTable
    height="250"
    fixed-header
  >
    <thead>
      <tr>
        <th class="text-uppercase">
          Patient ID
        </th>
        <th>
          Date of Entry
        </th>
        <th>
          Facility
        </th>
        <th>
          Inconsistency
        </th>
        <th>
          Data Team Action
        </th>
        <th>
          Date of Action
        </th>
      </tr>
    </thead>

    <tbody>
      <tr
        v-for="issue in data"
        :key="issue.id"
      >
        <td>
          {{ issue.patient_id }}
        </td>
        <td>
          {{ issue.date_of_entry }}
        </td>
        <td>
          {{ issue.facility_name }}
        </td>
        <td>
          {{ issue.inconsistency }}
        </td>
        <td>
          {{ issue.action_taken }}
        </td>
        <td>
          {{ issue.date_action_taken }}
        </td>
        <td />
      </tr>
    </tbody>
  </VTable>
</template>

