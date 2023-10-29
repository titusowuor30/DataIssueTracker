<script setup>
import axios from "@/axiosConfig"
import DQAnalytics from "@/views/dashboard/DQAnalytics.vue"
import Welcome from "@/views/dashboard/DQITsWelcome.vue"
import DataHistory from "@/views/dashboard/DataIssueHistory.vue"
import DataLogs from "@/views/dashboard/DataLogs.vue"

// 👉 Images

const all_issues = ref(0)
const pending_count = ref(0)
const matching_count = ref(0)
const corrected_count = ref(0)
const no_data_count = ref(0)
const available_count = ref(0)

const fetchData = () => {
  axios
    .get("data_issue_stats/")
    .then(response => {
      pending_count.value = response.data.pending
      all_issues.value = response.data.all_issues
      matching_count.value = response.data.matching
      corrected_count.value = response.data.corrected
      no_data_count.value = response.data.no_data
      available_count.value = response.data.available
    })
    .catch(error => {
      console.error("Error fetching data:", error)
    })
}

onMounted(() => {
  fetchData()
})
</script>

<template>
  <VRow>
    <!-- 👉 Congratulations -->
    <VCol
      cols="12"
      md="8"
    >
      <Welcome />
    </VCol>

    <VCol
      cols="12"
      sm="4"
    >
      <VRow>
        <!-- 👉  -->
        <VCol
          cols="12"
          md="6"
        >
          <CardStatisticsVertical
            v-bind="{
              title: 'All Issues',
              image: 'bx-bar-chart',
              style: 'bg-primary',
              stats: new Intl.NumberFormat().format(all_issues),
              change: Number((all_issues / all_issues) * 100).toFixed(2),
            }"
          />
        </VCol>

        <!-- 👉 Sales -->
        <VCol
          cols="12"
          md="6"
        >
          <CardStatisticsVertical
            v-bind="{
              title: 'Pending',
              style: 'bg-info',
              image: 'bx-line-chart',
              stats: new Intl.NumberFormat().format(pending_count),
              change: Number((pending_count / all_issues) * 100).toFixed(2),
            }"
          />
        </VCol>
      </VRow>
    </VCol>

    <!-- 👉 Analytics -->
    <VCol
      cols="12"
      md="8"
      order="2"
      order-md="1"
    >
      <DQAnalytics />
    </VCol>

    <VCol
      cols="12"
      sm="8"
      md="4"
      order="1"
      order-md="2"
    >
      <VRow>
        <!-- 👉 Payments -->
        <VCol
          cols="12"
          sm="6"
        >
          <CardStatisticsVertical
            v-bind="{
              title: 'Data already available',
              image: 'bx-data',
              style: 'bg-info',
              stats: new Intl.NumberFormat().format(available_count),
              change: Number((available_count / all_issues) * 100).toFixed(2),
            }"
          />
        </VCol>

        <!-- 👉  -->
        <VCol
          cols="12"
          sm="6"
        >
          <CardStatisticsVertical
            v-bind="{
              title: 'Entry Corrected',
              style: 'bg-primary',
              image: 'bx-check',
              stats: new Intl.NumberFormat().format(corrected_count),
              change: Number((corrected_count / all_issues) * 100).toFixed(2),
            }"
          />
        </VCol>
        <!-- 👉  -->
        <VCol
          cols="12"
          sm="6"
        >
          <CardStatisticsVertical
            v-bind="{
              title: 'Matching src doc',
              style: 'bg-primary',
              image: 'bx-file',
              stats: new Intl.NumberFormat().format(matching_count),
              change: Number((matching_count / all_issues) * 100).toFixed(2),
            }"
          />
        </VCol>
        <VCol
          cols="12"
          sm="6"
        >
          <CardStatisticsVertical
            v-bind="{
              title: 'No data needed',
              style: 'bg-info',
              image: 'bx-box',
              stats: new Intl.NumberFormat().format(no_data_count),
              change: Number((no_data_count / all_issues) * 100).toFixed(2),
            }"
          />
        </VCol>
      </VRow>
    </VCol>

    <!-- 👉 Data tbalees -->
    <VCol
      cols="12"
      md="8"
      sm="6"
      order="2"
    >
      <DataHistory />
    </VCol>
    <!-- 👉 logs -->
    <VCol
      cols="12"
      md="4"
      sm="6"
      order="2"
    >
      <DataLogs />
    </VCol>
  </VRow>
</template>
