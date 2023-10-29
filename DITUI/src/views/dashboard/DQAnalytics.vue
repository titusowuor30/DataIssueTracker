<script setup>
import { hexToRgb } from '@layouts/utils'
import VueApexCharts from 'vue3-apexcharts'
import {
  useDisplay,
  useTheme,
} from 'vuetify'
import { ref, onMounted, onUnmounted } from 'vue'
import axios from "@/axiosConfig"

const currentYear = ref(new Date().getFullYear())
const years = ref(Array.from({ length: currentYear.value - 2019 }, (_, index) => 2020 + index))
const selectedYear = ref('All')
const selectedAction = ref('All')
const facilities=ref([])
const facility = ref('All')
const series = ref([])
const convertion_ratio=ref(0)


const fetchFacilities = async()=>{
  await axios.get(`facilities`)
    .then(response=>{
      facilities.value = response.data['results'].sort((a, b) => a.facility_name.localeCompare(b.facility_name)).map(x=>x.facility_name)
      facilities.value.unshift("All")
      facilities.value
    })
    .catch(error=>{
      console.log(error)
      facilities.value = []
    })
}

// Function to fetch insights data based on filters
const fetchInsightsData = async () => {
  await axios.get(`analytics/?year=${selectedYear.value}&action_taken=${selectedAction.value}&facility=${facility.value}`)
    .then(response=>{
      series.value=response.data['series']
      convertion_ratio.value=response.data.conversion_ratio
    })    
    .catch(error=> {
      console.log(error)
      series.value = []
    })
}

// Fetch insights data when the component is mounted
onMounted(() => {
  fetchFacilities()
  fetchInsightsData()
  years.value.unshift("All")
})
  
const vuetifyTheme = useTheme()
const display = useDisplay()

const chartOptions = computed(() => {
  const currentTheme = vuetifyTheme.current.value.colors
  const variableTheme = vuetifyTheme.current.value.variables
  const disabledTextColor = `rgba(${ hexToRgb(String(currentTheme['on-surface'])) },${ variableTheme['disabled-opacity'] })`
  const primaryTextColor = `rgba(${ hexToRgb(String(currentTheme['on-surface'])) },${ variableTheme['high-emphasis-opacity'] })`
  const borderColor = `rgba(${ hexToRgb(String(variableTheme['border-color'])) },${ variableTheme['border-opacity'] })`

  return {
    bar: {
      chart: {
        stacked: true,
        parentHeightOffset: 0,
        toolbar: { show: false },
      },
      dataLabels: { enabled: false },
      stroke: {
        width: 6,
        lineCap: 'round',
        colors: [currentTheme.surface],
      },
      colors: [
        `rgba(${ hexToRgb(String(currentTheme.primary)) }, 1)`,
        `rgba(${ hexToRgb(String(currentTheme.info)) }, 1)`,
        `rgba(${ hexToRgb(String(currentTheme.warning)) }, 1)`,
        `rgba(${ hexToRgb(String(currentTheme.success)) }, 1)`,
        `rgba(${ hexToRgb(String(currentTheme.secondary)) }, 1)`,
        `rgba(${ hexToRgb(String(currentTheme.error)) }, 1)`,
      ],
      legend: {
        offsetX: -10,
        position: 'top',
        fontSize: '14px',
        horizontalAlign: 'left',
        fontFamily: 'Public Sans',
        labels: { colors: currentTheme.secondary },
        itemMargin: {
          vertical: 4,
          horizontal: 10,
        },
        markers: {
          width: 8,
          height: 8,
          radius: 10,
          offsetX: -4,
        },
      },
      states: {
        hover: { filter: { type: 'none' } },
        active: { filter: { type: 'none' } },
      },
      grid: {
        borderColor,
        padding: { bottom: 5 },
      },
      plotOptions: {
        bar: {
          borderRadius: 10,
          columnWidth: '30%',
          endingShape: 'rounded',
          startingShape: 'rounded',
        },
      },
      xaxis: {
        axisTicks: { show: true },
        crosshairs: { opacity: 0 },
        axisBorder: { show: true },
        categories: [
          'Jan',
          'Feb',
          'Mar',
          'Apr',
          'May',
          'Jun',
          'Jul',
          'Aug',
          'Sep',
          'Oct',
          'Nov',
          'Dec',
        ],
        labels: {
          style: {
            fontSize: '14px',
            colors: disabledTextColor,
            fontFamily: 'Public Sans',
          },
        },
      },
      yaxis: {
        labels: {
          style: {
            fontSize: '14px',
            colors: disabledTextColor,
            fontFamily: 'Public Sans',
          },
        },
      },
      responsive: [
        {
          breakpoint: display.thresholds.value.xl,
          options: { plotOptions: { bar: { columnWidth: '43%' } } },
        },
        {
          breakpoint: display.thresholds.value.lg,
          options: { plotOptions: { bar: { columnWidth: '50%' } } },
        },
        {
          breakpoint: display.thresholds.value.md,
          options: { plotOptions: { bar: { columnWidth: '42%' } } },
        },
        {
          breakpoint: display.thresholds.value.sm,
          options: { plotOptions: { bar: { columnWidth: '45%' } } },
        },
      ],
    },
    radial: {
      chart: { sparkline: { enabled: true } },
      labels: ['Conversion Rate'],
      stroke: { dashArray: 5 },
      colors: [`rgba(${ hexToRgb(String(currentTheme.primary)) }, 1)`],
      states: {
        hover: { filter: { type: 'none' } },
        active: { filter: { type: 'none' } },
      },
      fill: {
        type: 'gradient',
        gradient: {
          shade: 'dark',
          opacityTo: 0.6,
          opacityFrom: 1,
          shadeIntensity: 0.5,
          stops: [
            30,
            70,
            100,
          ],
          inverseColors: false,
          gradientToColors: [currentTheme.primary],
        },
      },
      plotOptions: {
        radialBar: {
          endAngle: 150,
          startAngle: -140,
          hollow: { size: '55%' },
          track: { background: 'transparent' },
          dataLabels: {
            name: {
              offsetY: 25,
              fontWeight: 600,
              fontSize: '16px',
              color: currentTheme.secondary,
              fontFamily: 'Public Sans',
            },
            value: {
              offsetY: -15,
              fontWeight: 500,
              fontSize: '24px',
              color: primaryTextColor,
              fontFamily: 'Public Sans',
            },
          },
        },
      },
      responsive: [
        {
          breakpoint: 900,
          options: { chart: { height: 200 } },
        },
        {
          breakpoint: 735,
          options: { chart: { height: 200 } },
        },
        {
          breakpoint: 660,
          options: { chart: { height: 200 } },
        },
        {
          breakpoint: 600,
          options: { chart: { height: 280 } },
        },
      ],
    },
  }
})

const balanceData = [
  {
    icon: 'bx-bar-chart',
    amount: `1236`,
    year: new Date().getFullYear(),
    color: 'primary',
  },
  {
    icon: 'bx-line-chart',
    amount: '2345',
    year: new Date().getFullYear()-1,
    color: 'info',
  },
]
</script>

<template>
  <VCard>
    <VRow no-gutters>
      <VCol
        cols="12"
        sm="7"
        xl="8"
        :class="$vuetify.display.smAndUp ? 'border-e' : 'border-b'"
      >
        {{ year1 }}
        <VCardItem class="pb-0">
          <VCardTitle>Data Quality Issues</VCardTitle>

          <template #append>
            <div class="me-n3">
              <MoreBtn />
            </div>
          </template>
        </VCardItem>

        <!-- bar chart -->
        <VueApexCharts
          id="bar-chart"
          type="bar"
          :height="336"
          :options="chartOptions.bar"
          :series="series"
        />
      </VCol>

      <VCol
        cols="12"
        sm="5"
        xl="4"
      >
        <VCardText class="text-center">
          <!-- Add a filter section to select year, action, and month -->
          <VCol
            cols="12"
            class="mt-4"
          >
            <VForm>
              <VRow
                align="center"
                class="py-2"
              >
                <VCol
                  cols="12"
                  sm="4"
                >
                  <VSelect
                    v-model="selectedYear"
                    label="Year"
                    :items="years"
                    @update:model-value="fetchInsightsData"
                  />
                </VCol>
                <VCol
                  cols="12"
                  sm="4"
                >
                  <VSelect
                    v-model="selectedAction"
                    label="Action Taken"
                    :items="['All','Entry Corrected', 'Data Matches Source Document', 'Data Already Available', 'No Data Needed', 'Pending']"
                    @update:model-value="fetchInsightsData"
                  />
                </VCol>
                <VCol
                  cols="12"
                  sm="4"
                >
                  <VSelect
                    v-model="facility"
                    label="Facility"
                    :items="facilities"
                    @update:model-value="fetchInsightsData"
                  />
                </VCol>
              </VRow>
            </VForm>
          </VCol>

          <!-- radial chart -->
          <VueApexCharts
            type="radialBar"
            :height="250"
            :options="chartOptions.radial"
            :series="[Number(convertion_ratio)]"
            class="mt-6"
          />
          <div class="d-flex align-center justify-center gap-x-8 gap-y-4 flex-wrap">
            <div
              v-for="data in balanceData"
              :key="data.year"
              class="d-flex align-center gap-3"
            >
              <VAvatar
                :icon="data.icon"
                :color="data.color"
                size="38"
                rounded
                variant="tonal"
              />

              <div class="text-start">
                <span class="text-sm"> {{ data.year }}</span>
                <h6 class="text-base font-weight-medium">
                  {{ data.value }}
                </h6>
              </div>
            </div>
          </div>
        </VCardText>
      </VCol>
    </VRow>
  </VCard>
</template>

<style lang="scss">
#bar-chart .apexcharts-series[rel="2"] {
  transform: translateY(-10px);
}
</style>
