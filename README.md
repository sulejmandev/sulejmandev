<a name="overview"></a>

<picture>
  <source media="(max-width: 600px)" srcset="assets/sulejman-mobile.gif">
  <img width="100%" src="assets/sulejman-desktop.gif" alt="Sulejman Alawashreh · Software Engineer · Amman, Jordan. I’m a software engineer who turns complex workflows into straightforward web applications. I design each feature around how data moves, how the pieces fit together, and what should happen when something goes wrong.">
</picture>

<p>
<a href="mailto:hello@sulejman.dev"><img width="200" src="assets/email.svg" alt="Send me an email"></a>
<a href="https://www.linkedin.com/in/sulejmandev/"><img width="200" src="assets/linkedin.svg" alt="Connect on LinkedIn"></a>
<a href="https://github.com/sulejmandev/portfolio"><img width="200" src="assets/portfolio.svg" alt="View code on GitHub"></a>
</p>

<picture>
  <source media="(max-width: 600px)" srcset="assets/stack-mobile.svg">
  <img width="100%" src="assets/stack-desktop.svg" alt="Front-end: TanStack Start, Next.js, TypeScript, Tailwind CSS. Back-end: Node.js, Express, Python, Go, Bun. Database: PostgreSQL, MongoDB. CI/CD: GitHub Actions and Git.">
</picture>

<a name="daily-challenge"></a>

<!-- daily-backend:start -->

<picture>
  <source media="(max-width: 600px)" srcset="assets/daily-mobile.svg">
  <img src="assets/daily.svg" width="100%" alt="One-minute back-end challenge · 26 Nov 2026 · Caching zero. How many times does this function read the stock?">
</picture>

<details>
<summary>Read or copy the function</summary>

How many times does this function read the stock?

```javascript
const cache = new Map();
let reads = 0;
function stock(sku) {
  if (cache.get(sku)) return cache.get(sku);
  reads++;
  cache.set(sku, 0);
  return 0;
}
stock("A"); stock("A");
console.log(reads);
```

</details>

<details>
<summary><strong>Reveal the answer</strong></summary>

<p>Output: <code>2</code></p>
<p>A stock count of 0 is falsy, so both calls miss the cache check. Use cache.has(sku) to distinguish a cached zero from a missing entry.</p>

</details>

<!-- daily-backend:end -->

<p align="right"><a href="#overview">Back to top ↑</a></p>
