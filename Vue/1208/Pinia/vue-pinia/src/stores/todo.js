import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

// TODO store 작성 (이름 counter 아니어도 ok)
export const useTodoStore = defineStore('todo', () => {
  let id = 0

  const todos = ref([
    { id: id++, text: 'Todo 1', isDone: false },
    { id: id++, text: 'Todo 2', isDone: false },
  ])

  const addTodo = function (todoText) {
    todos.value.push({
      id: id++,
      text: todoText,
      isDone: false,
  })
  }

  const deleteTodo = function (selectedId) {
    // findindex 메서드 활용한 삭제
    const index = todos.value.findIndex(todo => todo.id === selectedId)
    todos.value.splice(index, 1)
  }

  const updateTodo = function (selectedId) {
    todos.value.forEach((todo) => {
      if (todo.id === selectedId) {
        todo.isDone = !todo.isDone  // 토글하기
      }
    })
  }

  const doneTodoCount = computed(() => {
    const doneTodo = todos.value.filter(todo => todo.isDone)
    return doneTodo.length
  })

  return { 
    todos,
    addTodo,
    deleteTodo,
    updateTodo,
    doneTodoCount
   }
}, { persist: true })  // persist 옵션 추가
