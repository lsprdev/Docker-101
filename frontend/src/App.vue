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
      @keydown.enter="onEnterPress"
    />
    <ItemList :items="items" @delete="onDelete" />
  </header>
</template>

<script>
import { convertTypeAcquisitionFromJson } from "typescript";
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
      baseUrl: "http://localhost:8000",
    };
  },
  mounted() {
    this.getItems();
  },
  methods: {
    async onEnterPress(event) {
      if (event.key === "Enter" && this.inputValue.trim() !== "") {
        event.preventDefault();
        if (!this.isAddingItem) {
          this.isAddingItem = true;
          await this.addItem();
          this.isAddingItem = false;
        }
      }
    },
    async addItem() {
      try {
        const response = await fetch(`${this.baseUrl}/itens/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ name: this.inputValue }),
        });
        if (response.ok) {
          const data = await response.json();
          this.items.push(data);
          this.inputValue = "";
        } else {
          throw new Error("Erro ao adicionar item");
        }
      } catch (error) {
        console.error(error);
      }
    },
    async onDelete(item) {
      try {
        const response = await fetch(`${this.baseUrl}/itens/${item}/`, {
          method: "DELETE",
        });
        if (response.ok) {
          this.items = this.items.filter((i) => i.name !== item);
          this.getItems();
        } else {
          throw new Error("Erro ao deletar item");
        }
      } catch (error) {
        console.error(error);
      }
    },
    async getItems() {
      try {
        const response = await fetch(`${this.baseUrl}/itens/?format=json`);
        const data = await response.json();
        this.items = data;
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
