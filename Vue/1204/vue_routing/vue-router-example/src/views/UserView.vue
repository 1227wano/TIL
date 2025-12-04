<template>
    <div>
        <h3>User View</h3>
        <p>{{ userId }}번 유저</p>
        <RouterLink :to="{ name: 'profile' }">Profile</RouterLink>
        <RouterLink :to="{ name: 'posts' }">Posts</RouterLink>
    </div>
    <hr>
    <button @click="goHome">홈으로</button>
    <RouterView />
</template>

<script setup>
import { useRoute, RouterLink, RouterView, useRouter } from 'vue-router'
import { ref } from 'vue'

const route = useRoute()
const userId = ref(route.params.id)

const router = useRouter()
const goHome = () => {
    router.push({ name: 'home' })
    // router.replace({ name: 'home' })
}
</script>

<style scoped>

</style>