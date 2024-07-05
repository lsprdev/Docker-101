<template>
  <div>
    <h2 class="text-lg font-semibold mb-2">Listagem de Itens:</h2>
    <ul class="list-disc pl-5">
      <li v-for="(item, index) in items" :key="index">
        {{ item.name }}
        <button @click="handleDeletion(item.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ItemList",
  props: {
    items: {
      type: Array,
      required: true,
    },
  },
  methods: {
    handleDeletion(id) {
      this.$emit("delete", id);
    },
  },
};
</script>

<style scoped>
/* Optionally, add default styling or leave it unstyled for customization */
</style>
