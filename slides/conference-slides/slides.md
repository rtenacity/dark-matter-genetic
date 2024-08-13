---
theme: frankfurt
colorSchema: light
author: Mu-Tsun Tsai
date: 2023/01/01
transition: slide-left
---

# Slidev Theme Frankfurt

Presentation slides for developers

<div class="pt-12">
  <span @click="next" class="px-2 p-1 rounded cursor-pointer hover:bg-white hover:bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

---
section: Introduction
---

# What is Slidev?

Slidev is a slides maker and presenter designed for developers, consist of the following features

- 📝 **Text-based** - focus on the content with Markdown, and then style them later
- 🎨 **Themable** - theme can be shared and used with npm packages
- 🧑‍💻 **Developer Friendly** - code highlighting, live coding with autocompletion
- 🤹 **Interactive** - embedding Vue components to enhance your expressions
- 🎥 **Recording** - built-in recording and camera view
- 📤 **Portable** - export into PDF, PNGs, or even a hostable SPA
- 🛠 **Hackable** - anything possible on a webpage

<br>
<br>

Read more about [Why Slidev?](https://sli.dev/guide/why)


---

# Navigation


<Item title="Title of your thing">
	Create a box for definitions, lemmas, theorems, etc.
</Item>

---

# Code





<Item title="Neutral meson decay">
  <div class="image-container">
    <img class="feynman" src="./feynman1.png" alt="Feynman Diagram 1" width="300" height="auto">
  </div>
</Item>

<style> 
.image-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.feynman {
  border-radius: 10px;
}
</style>


---
section: Final words
layout: center
class: "text-center"
---

# Learn More

[Documentations](https://sli.dev) / [GitHub Repo](https://github.com/slidevjs/slidev)