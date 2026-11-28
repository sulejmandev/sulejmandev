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
  <img src="assets/daily.svg" width="100%" alt="One-minute back-end challenge · 28 Nov 2026 · Async filtering. Only job 2 is ready. Which IDs does this return?">
</picture>

<details>
<summary>Read or copy the function</summary>

Only job 2 is ready. Which IDs does this return?

```javascript
function readyJobs(ids) {
  return ids.filter(async id => id === 2);
}
console.log(readyJobs([1, 2]).join(","));
```

</details>

<details>
<summary><strong>Reveal the answer</strong></summary>

<p>Output: <code>1,2</code></p>
<p>filter checks the callback result immediately. Both promises are truthy, even the one that resolves to false. Await the readiness checks before filtering.</p>

</details>

<!-- daily-backend:end -->

<p align="right"><a href="#overview">Back to top ↑</a></p>
