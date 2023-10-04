<template>
  <div class="h-100 d-flex align-center justify-space-between">
    <!-- 👉 Footer: left content -->
    <span class="d-flex align-center">
      &copy;
      {{ new Date().getFullYear() }}
      Made With
      <VIcon
        icon="bx-heart"
        color="error"
        size="1.25rem"
        class="mx-1"
      />
      By <a
        href="https://bengohub.co.ke"
        target="_blank"
        rel="noopener noreferrer"
        class="text-primary ms-1"
      >Codevertex Africa</a>
    </span>
    <!-- 👉 Footer: right content -->
    <span class="d-md-flex gap-x-4 text-primary d-none">DQITs Portal V1.0.0
    </span>
  </div>
</template>
