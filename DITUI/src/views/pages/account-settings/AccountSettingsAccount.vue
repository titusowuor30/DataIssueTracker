<script setup>
import avatar1 from "@images/avatars/avatar-1.png"
import { useStore } from "vuex"
import axios from "@/axiosConfig"
import Swal from "sweetalert2"


const store = useStore()
const user = ref(store.state.auth.user)
const imgbaseUrl = ref(store.state.setup.baseUrl)
const pic = ref("")
const refInputEl = ref(undefined)

pic.value = imgbaseUrl.value + user.value.profile_pic

console.log(user)

const timezones = [
  "(GMT-11:00) International Date Line West",
  "(GMT-11:00) Midway Island",
  "(GMT-10:00) Hawaii",
  "(GMT-09:00) Alaska",
  "(GMT-08:00) Pacific Time (US & Canada)",
  "(GMT-08:00) Tijuana",
  "(GMT-07:00) Arizona",
  "(GMT-07:00) Chihuahua",
  "(GMT-07:00) La Paz",
  "(GMT-07:00) Mazatlan",
  "(GMT-07:00) Mountain Time (US & Canada)",
  "(GMT-06:00) Central America",
  "(GMT-06:00) Central Time (US & Canada)",
  "(GMT-06:00) Guadalajara",
  "(GMT-06:00) Mexico City",
  "(GMT-06:00) Monterrey",
  "(GMT-06:00) Saskatchewan",
  "(GMT-05:00) Bogota",
  "(GMT-05:00) Eastern Time (US & Canada)",
  "(GMT-05:00) Indiana (East)",
  "(GMT-05:00) Lima",
  "(GMT-05:00) Quito",
  "(GMT-04:00) Atlantic Time (Canada)",
  "(GMT-04:00) Caracas",
  "(GMT-04:00) La Paz",
  "(GMT-04:00) Santiago",
  "(GMT-03:30) Newfoundland",
  "(GMT-03:00) Brasilia",
  "(GMT-03:00) Buenos Aires",
  "(GMT-03:00) Georgetown",
  "(GMT-03:00) Greenland",
  "(GMT-02:00) Mid-Atlantic",
  "(GMT-01:00) Azores",
  "(GMT-01:00) Cape Verde Is.",
  "(GMT+00:00) Casablanca",
  "(GMT+00:00) Dublin",
  "(GMT+00:00) Edinburgh",
  "(GMT+00:00) Lisbon",
  "(GMT+00:00) London",
]

const accountData = {
  id: user.value.id,
  username: user.value.username || user.value.email,
  email: user.value.email || "johnDoe@example.com",
  first_name: user.value.first_name || "john",
  last_name: user.value.last_name || "Doe",
  role: user.value.role,
  phone: user.value.phone || "+254 (743) 793-901",
  gender: "Other",
  profile_pic: user.value.profile_pic,
  organisation: "DQITs",
  fcm_token: "",
  address: user.value.address || "123 Main St, Nairobi, NY 10001",
  state: user.value.state || "Nairobi",
  zip: user.value.zip || "001",
  country: user.value.country || "Kenya",
  language: user.value.language || "English",
  timezone: user.value.timezone || "(GMT-11:00) International Date Line West",
}

const accountDataLocal = ref(structuredClone(accountData))

console.log(accountData)

const isAccountDeactivated = ref(false)

const resetForm = () => {
  accountDataLocal.value = structuredClone(accountData)
}

const changeAvatar = file => {
  const fileReader = new FileReader()
  const { files } = file.target
  if (files && files.length > 0) {
    fileReader.readAsDataURL(files[0])
    fileReader.addEventListener('load', () => {
      if (typeof fileReader.result === "string")
        console.log(fileReader.result)//accountDataLocal.value.profile_pic = fileReader.result
    })
  }
}

// reset avatar image
const resetAvatar = () => {
  accountDataLocal.value.profile_pic = accountData.profile_pic
}

const updateuser=()=>{
  axios.put(`usersapi/${user.value.id}/`, accountData).then(response=>{
    console.log(response.data)
    Swal.fire({
      icon: "success",
      title: "success!",
      html: "Process completed successfully",
      timer: 3000,
    }).finally(() => {
      Swal.close()
    })
  }).catch(error=>{
    console.log(error)
    Swal.fire({
      icon: "error",
      title: "Error!",
      html: error,
      timer: 5000,
    }).finally(() => {
      Swal.close()
    })
  })
}
</script>

<template>
  <VRow>
    <VCol cols="12">
      <VCard title="Account Details">
        <VCardText class="d-flex">
          <!-- 👉 Avatar -->
          <VAvatar
            rounded="sm"
            size="150"
            class="me-6"
            :image="accountDataLocal.profile_pic"
          />

          <!-- 👉 Upload Photo -->
          <form class="d-flex flex-column justify-center gap-5">
            <div class="d-flex flex-wrap gap-2">
              <VBtn
                color="primary"
                @click="refInputEl?.click()"
              >
                <VIcon
                  icon="bx-cloud-upload"
                  class="d-sm-none"
                />
                <span class="d-none d-sm-block">Upload new photo</span>
              </VBtn>

              <input
                ref="refInputEl"
                type="file"
                name="file"
                accept=".jpeg,.png,.jpg,GIF"
                hidden
                @input="changeAvatar"
              >

              <VBtn
                type="reset"
                color="error"
                variant="tonal"
                @click="resetAvatar"
              >
                <span class="d-none d-sm-block">Reset</span>
                <VIcon
                  icon="bx-refresh"
                  class="d-sm-none"
                />
              </VBtn>
            </div>

            <p class="text-body-1 mb-0">
              Allowed JPG, GIF or PNG. Max size of 800K
            </p>
          </form>
        </VCardText>

        <VDivider />

        <VCardText>
          <!-- 👉 Form -->
          <VForm class="mt-6">
            <VRow>
              <!-- 👉 First Name -->
              <VCol
                md="6"
                cols="12"
              >
                <VTextField
                  v-model="accountDataLocal.first_name"
                  placeholder="John"
                  label="First Name"
                />
              </VCol>

              <!-- 👉 Last Name -->
              <VCol
                md="6"
                cols="12"
              >
                <VTextField
                  v-model="accountDataLocal.last_name"
                  placeholder="Doe"
                  label="Last Name"
                />
              </VCol>

              <!-- 👉 Email -->
              <VCol
                cols="12"
                md="6"
              >
                <VTextField
                  v-model="accountDataLocal.email"
                  label="E-mail"
                  placeholder="johndoe@gmail.com"
                  type="email"
                />
              </VCol>

              <!-- 👉 Organization -->
              <VCol
                cols="12"
                md="6"
              >
                <VTextField
                  v-model="accountDataLocal.org"
                  label="Organization"
                  placeholder="DQITs"
                />
              </VCol>

              <!-- 👉 Phone -->
              <VCol
                cols="12"
                md="6"
              >
                <VTextField
                  v-model="accountDataLocal.phone"
                  label="Phone Number"
                  placeholder="+1 (917) 543-9876"
                />
              </VCol>

              <!-- 👉 Address -->
              <VCol
                cols="12"
                md="6"
              >
                <VTextField
                  v-model="accountDataLocal.address"
                  label="Address"
                  placeholder="123 Main St, New York, NY 10001"
                />
              </VCol>

              <!-- 👉 State -->
              <VCol
                cols="12"
                md="6"
              >
                <VTextField
                  v-model="accountDataLocal.state"
                  label="State"
                  placeholder="New York"
                />
              </VCol>

              <!-- 👉 Zip Code -->
              <VCol
                cols="12"
                md="6"
              >
                <VTextField
                  v-model="accountDataLocal.zip"
                  label="Zip Code"
                  placeholder="10001"
                />
              </VCol>

              <!-- 👉 Country -->
              <VCol
                cols="12"
                md="6"
              >
                <VSelect
                  v-model="accountDataLocal.country"
                  label="Country"
                  :items="['USA', 'Canada', 'UK', 'India', 'Australia']"
                  placeholder="Select Country"
                />
              </VCol>

              <!-- 👉 Language -->
              <VCol
                cols="12"
                md="6"
              >
                <VSelect
                  v-model="accountDataLocal.language"
                  label="Language"
                  placeholder="Select Language"
                  :items="['English', 'Spanish', 'Arabic', 'Hindi', 'Urdu']"
                />
              </VCol>

              <!-- 👉 Timezone -->
              <VCol
                cols="12"
                md="6"
              >
                <VSelect
                  v-model="accountDataLocal.timezone"
                  label="Timezone"
                  placeholder="Select Timezone"
                  :items="timezones"
                  :menu-props="{ maxHeight: 200 }"
                />
              </VCol>

              <!-- 👉 Form Actions -->
              <VCol
                cols="12"
                class="d-flex flex-wrap gap-4"
              >
                <VBtn @click="updateuser">
                  Save changes
                </VBtn>
                <VBtn
                  color="secondary"
                  variant="tonal"
                  type="reset"
                  @click.prevent="resetForm"
                >
                  Reset
                </VBtn>
              </VCol>
            </VRow>
          </VForm>
        </VCardText>
      </VCard>
    </VCol>

    <VCol cols="12">
      <!-- 👉 Deactivate Account -->
      <VCard title="Deactivate Account">
        <VCardText>
          <div>
            <VCheckbox
              v-model="isAccountDeactivated"
              label="I confirm my account deactivation"
            />
          </div>

          <VBtn
            :disabled="!isAccountDeactivated"
            color="error"
            class="mt-3"
          >
            Deactivate Account
          </VBtn>
        </VCardText>
      </VCard>
    </VCol>
  </VRow>
</template>
