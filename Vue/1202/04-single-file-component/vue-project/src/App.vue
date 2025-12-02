<template>
  <h1>App.vue</h1>
  <MyComponent />
  <!-- <my-component>이렇게도 가능</my-component> -->
</template>

<script setup>
// @ 는 src/ 를 가리키는 별칭
import MyComponent from '@/components/MyComponent.vue'
  
</script>

<style scoped>  
/* 위의 scopoed 를 빼면 전역 스타일이 된다. */
h1 {
  color: blue;
}
</style>
