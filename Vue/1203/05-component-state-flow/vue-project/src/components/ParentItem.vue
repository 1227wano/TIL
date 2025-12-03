<template>
    <div>
        <p>Parent Item</p>
        <div>{{ myProp.id }}:{{ myProp.name }}</div>
    </div>
</template>

<script setup>
// 받을걸 외부에서 사용하는 법
const props = defineProps({
    myProp: Object
});
console.log(props.myProp);
</script>

<style scoped>

</style>