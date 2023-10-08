<script setup lang="ts">
interface Props {
  title: string;
  image: string;
  style: string;
  stats: string;
  change: number;
}

const props = defineProps<Props>();

const isPositive = controlledComputed(
  () => props.change,
  () => Math.sign(props.change) === 1
);
</script>

<template>
  <VCard
    style="
      background: linear-gradient(
        90deg,
        rgb(251, 235, 255) 0%,
        rgb(240, 230, 225) 50%,
        rgb(240, 239, 237) 100%
      );
    "
  >
    <VCardText class="d-flex align-center pb-4">
      <VIcon size="42" :icon="props.image" class="text-warning" />
      <VSpacer />

      <MoreBtn size="x-small" class="me-n3 mt-n4" />
    </VCardText>

    <VCardText>
      <p class="mb-1">
        {{ props.title }}
      </p>
      <h5 class="text-h5 text-no-wrap mb-3 text-error">
        {{ props.stats }}
      </h5>
      <span
        :class="isPositive ? 'text-primary' : 'text-error'"
        class="d-flex align-center gap-1 text-sm"
      >
        <VIcon size="18" :icon="isPositive ? 'bx-up-arrow-alt' : 'bx-down-arrow-alt'" />
        {{ isPositive ? Math.abs(props.change) : props.change }}%
      </span>
    </VCardText>
  </VCard>
</template>
