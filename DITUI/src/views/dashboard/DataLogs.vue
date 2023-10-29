<script setup>
import chart from '@images/avatars/avatar-1.png'
import { onMounted } from 'vue'
import axios from "@/axiosConfig"
import { useStore } from "vuex"

const store = useStore()

const imgbaseUrl = ref(store.state.setup.baseUrl)
const logs = ref([])

const moreList = [
  {
    title: 'View All',
    value: '/system-logs',
  },
]


const loadData = () => {
  axios
    .get('user-logs', {
      params: {
        limit: 4,
        offset: 0,
      },
    })
    .then(response => {
      logs.value = response.data.results
    })
    .catch(error => {
      console.error("Error loading data:", error)
    })
}

onMounted(()=>{
  loadData()
})
</script>

<template>
  <VCard
    title="Recent Actions"
    class="overflow-auto"
    >
    <template #append>
      <div class="me-n3 mt-n2">
        <VBtn
          text="View All"
          to="/system-logs"
        />
      </div>
    </template>

    <VCardText>
      <VList class="card-list">
        <VListItem
          v-for="item in logs"
          :key="item.id"
        >
          <template #prepend>
            <VAvatar
              rounded
              variant="tonal"
              :color="item.color"
              :image="imgbaseUrl+item.user.profile_pic"
              class="me-3"
            />
          </template>

          <VListItemSubtitle class="text-disabled mb-1">
            {{ item.user.email }}
            <small>{{ item.timestamp.toLocaleString() }}</small>
          </VListItemSubtitle>
          <VListItemTitle>
            {{ item.action }}
          </VListItemTitle>

          <template #append>
            <VListItemAction>
              <VChip
                class="me-1"
                color="warning"
              >
                {{ item.title }}
              </VChip>
            </VListItemAction>
          </template>
        </VListItem>
        <p v-if="logs.length === 0">
          No Recent actions yet!
        </p>
      </VList>
    </VCardText>
  </VCard>
</template>

<style lang="scss" scoped>
  .card-list {
    --v-card-list-gap: 1.6rem;
  }
</style>
