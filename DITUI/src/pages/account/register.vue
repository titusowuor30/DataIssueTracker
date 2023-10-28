<script setup>
import AuthProvider from '@/views/pages/authentication/AuthProvider.vue'
import logo from '@images/icons/logo/triangle-dark.png'
import axios from  "@/axiosConfig"
import Swal from "sweetalert2"

const form = ref({
  username: '',
  email: '',
  account_information: '',
  privacyPolicies: false,
})

const isPasswordVisible = ref(false)

const submitRequest = async() =>{
  await axios.post('account-requests/', form.value)
    .then(response=>{
      console.log(response)
      Swal.fire({
        icon: "success",
        title: "success!",
        html: "<p>Request submitted successfully<br/>Someone from DQITs Team will get back to you soon!</p>",
        timer: 3000,
      }).finally(() => {
        Swal.close()
      })
    })

}
</script>

<template>
  <div class="auth-wrapper d-flex align-center justify-center pa-4">
    <VCard
      class="auth-card pa-4 pt-7"
      max-width="600"
    >
      <VCardItem class="justify-center">
        <template #prepend>
          <div class="d-flex">
            <RouterLink
              to="/login"
              class="app-logo d-flex align-center gap-x-3 app-title-wrapper"
            >
              <VImg
                :src="logo"
                class="d-flex img-fluid"
                :height="120"
                :width="200"
              />
            </RouterLink>
          </div>
        </template>
      </VCardItem>

      <VCardText class="pt-2 text-center">
        <h5 class="text-h5 mb-1">
          Adventure starts here 🚀
        </h5>
        <p class="mb-0">
          <em>Make your app management easy and fun!</em>
        </p>
      </VCardText>

      <VCardText>
        <VForm @submit.prevent="$router.push('/')">
          <VRow>
            <!-- Username -->
            <VCol cols="12">
              <VTextField
                v-model="form.username"
                autofocus
                label="Username"
                placeholder="Johndoe"
              />
            </VCol>
            <!-- email -->
            <VCol cols="12">
              <VTextField
                v-model="form.email"
                label="Email"
                placeholder="johndoe@email.com"
                type="email"
              />
            </VCol>

            <!-- password -->
            <VCol cols="12">
              <VTextarea
                v-model="form.account_information"
                label="Account Information"
                placeholder="Provide info about your account e.g timezone, phone,first name, last name, username..."
                type="text"
              />
              <div class="d-flex align-center mt-1 mb-4">
                <VCheckbox
                  id="privacy-policy"
                  v-model="form.privacyPolicies"
                  inline
                />
                <VLabel
                  for="privacy-policy"
                  style="opacity: 1;"
                >
                  <span class="me-1">I agree to</span>
                  <a
                    href="javascript:void(0)"
                    class="text-primary"
                  >privacy policy & terms</a>
                </VLabel>
              </div>

              <VBtn
                block
                @click="submitRequest"
              >
                Request Account
              </VBtn>
            </VCol>

            <!-- login instead -->
            <VCol
              cols="12"
              class="text-center text-base"
            >
              <span>Already have an account?</span>
              <RouterLink
                class="text-primary ms-2"
                to="/login"
              >
                Sign in instead
              </RouterLink>
            </VCol>

            <VCol
              cols="12"
              class="d-flex align-center"
            >
              <VDivider />
              <span class="mx-4">or</span>
              <VDivider />
            </VCol>

            <!-- auth providers -->
            <VCol
              cols="12"
              class="text-center"
            >
              <AuthProvider />
            </VCol>
          </VRow>
        </VForm>
      </VCardText>
    </VCard>
  </div>
</template>

<style lang="scss">
@use "@core/scss/template/pages/page-auth.scss";
</style>
