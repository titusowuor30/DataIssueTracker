<template>
  <VCard>
    <VCardTitle>Manage Password Policy</VCardTitle>
    <VCardText>
      <VForm @submit.prevent="savePasswordPolicy">
        <VTextField
          v-model="policy.min_length"
          label="Minimum Password Length"
          class="px-2 py-2"
        />
        <VTextField
          v-model="policy.min_uppercase_letters"
          label="Minimum Uppercase Letters"
          class="px-2 py-2"
        />
        <VTextField
          v-model="policy.min_lowercase_letters"
          label="Minimum Lowercase Letters"
          class="px-2 py-2"
        />
        <VTextField
          v-model="policy.min_digits"
          label="Minimum Digits"
          class="px-2 py-2"
        />
        <VTextField
          v-model="policy.min_special_characters"
          label="Minimum Special Characters"
          class="px-2 py-2"
        />
        <VBtn
          type="submit"
          color="primary"
          class="px-2 py-2"
        >
          Save Policy
        </VBtn>
      </VForm>
    </VCardText>
  </VCard>
</template>

<script setup>
import { ref } from "vue"

const policy = ref({
  min_length: 8,
  min_uppercase_letters: 1,
  min_lowercase_letters: 1,
  min_digits: 1,
  min_special_characters: 0,
})

const savePasswordPolicy = () => {
  // Implement logic to save the password policy here
}
</script>
