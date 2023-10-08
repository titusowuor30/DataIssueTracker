<template>
  <VIcon
    size="40"
    style="color: green;"
    icon="bxs-file-import"
    @click="exportToCSV"
  />
</template>

<script setup>
import { defineEmits, defineProps } from "vue"

const props = defineProps({
  filename: String, // Receive the filename as a prop
  data: Array, // Receive the data as a prop (an array of arrays)
})

const emit = defineEmits(["export-csv"]) // Define a custom event

const exportToCSV = () => {
  // Emit the custom event 'export-csv' with filename and data as payload
  emit("export-csv", { filename: props.filename, data: props.data })
}
</script>
