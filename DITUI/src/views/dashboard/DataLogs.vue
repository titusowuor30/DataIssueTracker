<script setup>
import chart from '@images/avatars/avatar-1.png'

const logs = [
  {
    user: 'John Doe',
    issueType: 'Data Inaccuracy',
    description: 'Inaccurate customer records',
    color: 'error',
    timestamp: '2023-10-01 09:15:00',
  },
  {
    user: 'John Doe',
    issueType: 'Data Duplication',
    description: 'Duplicate entries in the database',
    color: 'error',
    timestamp: '2023-10-02 14:30:00',
  },
  {
    user: 'John Doe',
    issueType: 'Data Integrity',
    description: 'Data integrity violation detected',
    color: 'error',
    timestamp: '2023-10-03 11:45:00',
  },
  {
    user: 'John Doe',
    issueType: 'Data Completeness',
    description: 'Incomplete data in customer profiles',
    color: 'error',
    timestamp: '2023-10-04 16:20:00',
  },
  {
    user: 'John Doe',
    issueType: 'Data Consistency',
    description: 'Inconsistent data across systems',
    color: 'error',
    timestamp: '2023-10-05 08:50:00',
  },
]

const moreList = [
  {
    title: 'Share',
    value: 'Share',
  },
  {
    title: 'Refresh',
    value: 'Refresh',
  },
  {
    title: 'Update',
    value: 'Update',
  },
]
</script>

<template>
  <VCard title="DQITs Logs">
    <template #append>
      <div class="me-n3 mt-n2">
        <MoreBtn :menu-list="moreList" />
      </div>
    </template>

    <VCardText>
      <VList class="card-list">
        <VListItem
          v-for="item in logs"
          :key="item.timestamp"
        >
          <template #prepend>
            <VAvatar
              rounded
              variant="tonal"
              :color="item.color"
              :image="chart"
              class="me-3"
            />
          </template>

          <VListItemSubtitle class="text-disabled mb-1">
            {{ item.user }} - {{ item.timestamp }}
          </VListItemSubtitle>
          <VListItemTitle>
            {{ item.description }}
          </VListItemTitle>

          <template #append>
            <VListItemAction>
              <VChip
                class="me-1"
                color="warning"
              >
                {{ item.issueType }}
              </VChip>
            </VListItemAction>
          </template>
        </VListItem>
      </VList>
    </VCardText>
  </VCard>
</template>

<style lang="scss" scoped>
  .card-list {
    --v-card-list-gap: 1.6rem;
  }
</style>
