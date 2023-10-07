<script setup>
import AuthProvider from '@/views/pages/authentication/AuthProvider.vue'
import logo from '@images/icons/logo/triangle-dark.png'
import Swal from 'sweetalert2'
import { useStore } from 'vuex'

const form = ref({
  email: '',
  password: '',
  remember: false,
})

const isPasswordVisible = ref(false)

const store = useStore()
const router = useRouter()

const handleLogin = async () => {
  try {
    Swal.fire({
      icon: 'warning',
      title: "Please Wait!",
      html: "Authenticating your credentials...", // add html attribute if you want or remove
      allowOutsideClick: false,
      showConfirmButton: false,
      willOpen: () => {
        Swal.showLoading()
      },
    })

    const { email, password } = form.value // Extract email and password from the form

    console.log(form.value)
    await store.dispatch('auth/login', { email: email, password: password })

    // Login successful, navigate to another route or do something else
    Swal.fire({
      icon: 'success',
      title: 'Login successful!',
      html: 'Redirecting to DQITs Dashboard...',
      showConfirmButton: false,
      timer: 3000,
    })
    router.push('/')

    Swal.close()
  } catch (error) {
    // Login error, show error message
    console.error('Login error:', error)

    Swal.fire({
      icon: 'error',
      title: 'Login failed',
      html: error || 'An error occurred while logging in.',
    })
  }
}
</script>

<template>
  <div class="auth-wrapper d-flex align-center justify-center pa-4">
    <VCard
      class="auth-card pa-4 pt-7"
      max-width="448"
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

      <VCardText class="pt-2  text-center">
        <h5 class="text-h5 mb-1">
          Welcome to DQITs! 👋🏻
        </h5>
        <p class="mb-0">
          <em>Please sign-in to your account to proceed</em>
        </p>
      </VCardText>

      <VCardText>
        <VForm @submit.prevent="handleLogin">
          <VRow>
            <!-- email -->
            <VCol cols="12">
              <VTextField
                v-model="form.email"
                autofocus
                placeholder="johndoe@email.com"
                label="Email"
                type="email"
              />
            </VCol>

            <!-- password -->
            <VCol cols="12">
              <VTextField
                v-model="form.password"
                label="Password"
                placeholder="············"
                :type="isPasswordVisible ? 'text' : 'password'"
                :append-inner-icon="isPasswordVisible ? 'bx-hide' : 'bx-show'"
                @click:append-inner="isPasswordVisible = !isPasswordVisible"
              />

              <!-- remember me checkbox -->
              <div class="d-flex align-center justify-space-between flex-wrap mt-1 mb-4">
                <VCheckbox
                  v-model="form.remember"
                  label="Remember me"
                />

                <RouterLink
                  class="text-primary ms-2 mb-1"
                  to="javascript:void(0)"
                >
                  Forgot Password?
                </RouterLink>
              </div>

              <!-- login button -->
              <VBtn
                block
                type="submit"
              >
                Login
              </VBtn>
            </VCol>

            <!-- create account -->
            <VCol
              cols="12"
              class="text-center text-base"
            >
              <span>New on our platform?</span>
              <RouterLink
                class="text-primary ms-2"
                to="/register"
              >
                Request an account
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
