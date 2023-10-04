<script setup>
import illustrationDataQualityDark from '@images/cards/illustration-john-dark.png'
import illustrationDataQualityLight from '@images/cards/illustration-john-light.png'
import { useTheme } from 'vuetify'

const { global } = useTheme()
const illustrationDataQuality = computed(() => global.name.value === 'dark' ? illustrationDataQualityDark : illustrationDataQualityLight)
</script>

<template>
  <VCard class="text-center text-sm-start">
    <VRow no-gutters>
      <VCol
        cols="12"
        sm="8"
        order="2"
        order-sm="1"
      >
        <VCardItem>
          <VCardTitle class="text-md-h5 text-primary">
            Welcome to the Data Quality Issue Tracker Dashboard! 📊
          </VCardTitle>
        </VCardItem>

        <VCardText>
          <span>
            Stay on top of data quality issues and ensure data accuracy.
            <br>
            Track, manage, and resolve data quality concerns with ease.
          </span>
          <br>
          <VBtn
            variant="tonal"
            class="mt-4"
            size="small"
          >
            Get Started
          </VBtn>
        </VCardText>
      </VCol>

      <VCol
        cols="12"
        sm="4"
        order="1"
        order-sm="2"
        class="text-center"
      >
        <img
          :src="illustrationDataQuality"
          :height="$vuetify.display.xs ? '150' : '175'"
          :class="$vuetify.display.xs ? 'mt-6 mb-n2' : 'position-absolute'"
          class="data-quality-illustration flip-in-rtl"
        >
      </VCol>
    </VRow>
  </VCard>
</template>

<style lang="scss" scoped>
.data-quality-illustration {
  inset-block-end: -0.0625rem;
  inset-inline-end: 3rem;
}
</style>
