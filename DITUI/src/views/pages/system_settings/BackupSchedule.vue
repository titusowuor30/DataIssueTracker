<template>
  <VContainer>
    <VCard>
      <VCardTitle>Manage Backup Schedule</VCardTitle>
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
              <div class="form-group">
                <label for="exampleInputEmail1">Start Date</label>
                <input
                  id="start_date"
                  type="datetime-local"
                  class="form-control p-3 m-2"
                  v-model="schedule.start_date"
                  :placeholder="schedule.start_date"
                />
              </div>
              <div class="form-group">
                <label for="exampleInputEmail1">Last Run Date</label>
                <input
                  id="last_run_date"
                  type="datetime-local"
                  class="form-control p-3 m-2"
                  v-model="schedule.last_run_date"
                  placeholder="Last Run Date"
                />
              </div>
              <div class="form-group">
                <label for="exampleInputEmail1">Next Run Date</label>
                <input
                  id="next_run_date"
                  type="datetime-local"
                  class="form-control p-3 m-2"
                  v-model="schedule.next_run_date"
                  placeholder="Next Run Date"
                />
              </div>
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

const schedule = ref({
  task_type: "backup",
  schedule_type: "daily",
  start_date: new Date(),
  last_run_date: new Date(),
  next_run_date: new Date(),
  destination_path: "",
  source_path: "",
});

const taskTypes = ["backup", "restore"];
const scheduleTypes = ["daily", "weekly", "monthly"];

const saveBackupSchedule = () => {
  // Implement logic to save the backup schedule here
};
</script>
