<template>
    <div :class="wrapperClass">
        <input
        :id="id"
        :type="type"
        :name="name"
        :placeholder="placeholder"
        :value="modelValue"
        :class="inputClass"
        @input="$emit('update:modelValue', $event.target.value)"
        @focus="handleFocus"
        @blur="handleBlur"
        @keydown="handleKeydown"
        />
        <label v-if="label" :for="id" :class="labelClass">{{ label }}</label>
    </div>
</template>

<script>
export default {
  name: "InputBar",
  props: {
    modelValue: {
      type: String,
      default: "",
    },
    id: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
    type: {
      type: String,
      default: "text",
    },
    placeholder: {
      type: String,
      default: "",
    },
    label: {
      type: String,
      default: "",
    },
    inputClass: {
      type: String,
      default: "",
    },
    labelClass: {
      type: String,
      default: "",
    },
    wrapperClass: {
      type: String,
      default: "",
    },
  },
  methods: {
    handleFocus(event) {
      this.$emit("focus", event);
    },
    handleBlur(event) {
      this.$emit("blur", event);
    },
    handleKeydown(event) {
      this.$emit("keydown", event);
    },
  },
};
</script>

<style scoped>
/* Optionally, add default styling or leave it unstyled for customization */
</style>