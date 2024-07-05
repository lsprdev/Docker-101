<template>
  <header class="flex flex-col items-center p-4 w-full">
    <InputBar
      v-model="inputValue"
      id="input"
      name="input"
      placeholder="Adicione um Item..."
      inputClass="border border-gray-300 p-2 rounded-lg focus:outline-none focus:border-blue-500 w-72"
      labelClass="block text-sm font-medium text-gray-700 mb-1"
      wrapperClass="mb-4"
      @keydown="onKeydown"
    />
    <ItemList :items="items" />
  </header>
</template>

<script>
import InputBar from "./components/InputBar.vue";
import ItemList from "./components/ItemList.vue";

export default {
  name: "ParentComponent",
  components: {
    InputBar,
    ItemList,
  },
  data() {
    return {
      inputValue: "",
      items: [],
    };
  },
  methods: {
    onKeydown(event) {
      if (event.key === "Enter" && this.inputValue.trim() !== "") {
        this.addItem();
      }
    },
    addItem() {
      this.items.push(this.inputValue.trim());
      this.inputValue = "";
    },
  },
};
</script>
