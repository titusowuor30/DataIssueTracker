<template>
  <VContainer class="bg-primary">
    <VRow class="bg-secondary p-2">
      <VCol cols="6">
        <VBtn
          class="mdi-sync"
          @click="syncData"
        >
          Sync Data
        </VBtn>
      </VCol>
      <VCol cols="6">
        <p class="p-2">{{ sync_status }}</p>
      </VCol>
    </VRow>
    <VCard>
      <VCardTitle>Manage Data Sync Schedule</VCardTitle>
      <VCardText>
        <VForm @submit.prevent="saveBackupSchedule">
          <VRow>
            <VCol cols="6">
              <VSelect
                v-model="schedule.task_type"
                :items="taskTypes"
                label="Task Type"
              />
              <VSelect
                v-model="schedule.schedule_type"
                :items="scheduleTypes"
                label="Schedule Type"
              />
              <VTextField v-model="schedule.destination_path" label="Destination Path" />
              <VTextField
                v-model="schedule.source_path"
                class="py-2"
                label="Source Path"
              />
            </VCol>
            <VCol cols="6">
              <input
                id="start_date"
                v-model="schedule.start_date"
                type="datetime-local"
                class="form-control p-3 m-2"
                placeholder="Start Date"
              >
              <input
                id="last_run_date"
                v-model="schedule.last_run_date"
                type="datetime-local"
                class="form-control p-3 m-2"
                placeholder="Last Run Date"
              >
              <input
                id="next_run_date"
                v-model="schedule.next_run_date"
                type="datetime-local"
                class="form-control p-3 m-2"
                placeholder="Next Run Date"
              >
              <VCheckbox v-model="schedule.enabled" class="p-2" label="Enabled" />
            </VCol>
          </VRow>
          <VBtn type="submit" color="primary" class="p-2"> Save Schedule </VBtn>
        </VForm>
      </VCardText>
    </VCard>
  </VContainer>
</template>

<script setup>
import { ref } from "vue";
import axios from "@/axiosConfig";

const schedule = ref({
  task_type: "backup",
  schedule_type: "daily",
  start_date: new Date(),
  last_run_date: new Date(),
  next_run_date: new Date(),
  destination_path: "",
  source_path: "",
})
const sync_status=ref("")

const taskTypes = ["backup", "restore"];
const scheduleTypes = ["daily", "weekly", "monthly"];

const saveBackupSchedule = () => {
  // Implement logic to save the backup schedule here
}

const syncData=()=>{
  axios.post('sync_data/')
    .then(response=>{
      sync_status.value=response.data
    }).catch(error=>{
      sync_status.value=error
    })
}
</script>
