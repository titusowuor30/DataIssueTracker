<script setup>
const dataQualityIssues = [
  {
    Country: 'United States',
    'Facility Name': 'XYZ Hospital',
    Code: 'DQ-001',
    Inconsistency: 'Missing patient records',
    'Date of Entry': '2023-10-05',
    'Data Team Action': 'Investigation initiated',
  },
  {
    Country: 'Canada',
    'Facility Name': 'ABC Clinic',
    Code: 'DQ-002',
    Inconsistency: 'Duplicate patient IDs',
    'Date of Entry': '2023-10-07',
    'Data Team Action': 'Data cleanup in progress',
  },
  {
    Country: 'Australia',
    'Facility Name': 'LMN Hospital',
    Code: 'DQ-003',
    Inconsistency: 'Incorrect patient ages',
    'Date of Entry': '2023-10-10',
    'Data Team Action': 'Data validation ongoing',
  },
  {
    Country: 'United Kingdom',
    'Facility Name': 'PQR Clinic',
    Code: 'DQ-004',
    Inconsistency: 'Mismatched patient genders',
    'Date of Entry': '2023-10-12',
    'Data Team Action': 'Data correction initiated',
  },
  {
    Country: 'Germany',
    'Facility Name': 'NOP Hospital',
    Code: 'DQ-005',
    Inconsistency: 'Incomplete patient contact details',
    'Date of Entry': '2023-10-15',
    'Data Team Action': 'Data enrichment in progress',
  },
]
</script>

<template>
  <VTable
    height="250"
    fixed-header
  >
    <thead>
      <tr>
        <th class="text-uppercase">
          Country
        </th>
        <th>
          Facility Name
        </th>
        <th>
          Facility Code
        </th>
        <th>
          Inconsistency
        </th>
        <th>
          Date of Entry
        </th>
        <th>
          Data Team Action
        </th>
      </tr>
    </thead>

    <tbody>
      <tr
        v-for="issue in dataQualityIssues"
        :key="issue.Code"
      >
        <td>
          {{ issue.Country }}
        </td>
        <td>
          {{ issue['Facility Name'] }}
        </td>
        <td>
          {{ issue.Code }}
        </td>
        <td>
          {{ issue.Inconsistency }}
        </td>
        <td>
          {{ issue['Date of Entry'] }}
        </td>
        <td>
          {{ issue['Data Team Action'] }}
        </td>
        <td>
          {{ issue.Date }}
        </td>
      </tr>
    </tbody>
  </VTable>
</template>

