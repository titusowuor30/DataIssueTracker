<script setup>
import DQAnalytics from '@/views/dashboard/DQAnalytics.vue'
import Welcome from '@/views/dashboard/DQITsWelcome.vue'
import DataHistory from '@/views/dashboard/DataIssueHistory.vue'
import DataLogs from '@/views/dashboard/DataLogs.vue'

// 👉 Images
import chart from '@images/cards/chart-success.png'
import card from '@images/cards/credit-card-primary.png'
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
              image: chart,
              stats: '12,628',
              change: 72.80,
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
              image: chart,
              stats: '479',
              change: 28.42,
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
            v-bind=" {
              title: 'Data already available',
              image: chart,
              stats: '2,468',
              change: -14.82,
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
              image: card,
              stats: '4,857',
              change: 28.14,
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
              image: card,
              stats: '1,857',
              change: 28.14,
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
              image: card,
              stats: '187',
              change: 28.14,
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
