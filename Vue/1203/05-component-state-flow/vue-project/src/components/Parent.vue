<template>
    <div>
        <h1>Parent's Name: {{ name }}</h1>
        <Child 
            propsName="I'm the parent" 
            @some-event="someCallback"
            @emit-args="getNumbers"
            @update-name="updateName"
        />
        <hr>
        <ParentItem 
            v-for="item in items" 
            :key="item.id" 
            :my-prop="item"
        />
    </div>
</template>

<script setup>
import Child from '@/components/Child.vue';
import ParentItem from '@/components/ParentItem.vue';

import { ref } from 'vue';

const items = ref([
    { id: 1, name: 'apple' },
    { id: 2, name: 'banana' },
    { id: 3, name: 'cherry' }
])
const name = ref('Alice')

const someCallback = function() {
    alert('someEvent emitted!');
}

const getNumbers = function(...numbers) {
    console.log('get numbers!', numbers)
}

const updateName = function() {
    name.value = 'Bella'
}
</script>

<style scoped>

</style>