<p><img width="100%" src="assets/identity.png" alt="Sulejman Alawashreh · Software Engineer · Amman, Jordan"></p>

<p>I’m a software engineer who turns complex workflows into straightforward web applications. I design each feature around how data moves, how the pieces fit together, and what should happen when something goes wrong.</p>

<p>
  <a href="mailto:hello@sulejman.dev"><img src="assets/email.svg" width="252" alt="Send me an email"></a>
  <a href="https://www.linkedin.com/in/sulejmandev/"><img src="assets/linkedin.svg" width="252" alt="Connect on LinkedIn"></a>
  <a href="https://github.com/sulejmandev/portfolio"><img src="assets/portfolio.svg" width="252" alt="View code on GitHub"></a>
</p>

<h2>My stack</h2>

<p><img width="49%" src="assets/stack-0.png" alt="Front-end — TanStack Start, Next.js, TypeScript, Tailwind CSS" title="TanStack Start, Next.js, TypeScript, Tailwind CSS"> <img width="49%" src="assets/stack-1.png" alt="Back-end — Node.js, Express, Python, Go, Bun" title="Node.js, Express, Python, Go, Bun"><br>
<img width="49%" src="assets/stack-2.png" alt="Database — PostgreSQL, MongoDB" title="PostgreSQL, MongoDB"> <img width="49%" src="assets/stack-3.png" alt="CI/CD — GitHub Actions, Git" title="GitHub Actions, Git"></p>

<h2>One-minute back-end challenge</h2>

<!-- daily-backend:start -->

<p><sub>22 Nov 2026 · Retries</sub></p>

<p><strong>A client sends a payment request and times out. Is it safe to send exactly the same request again?</strong></p>

<details>
<summary>Reveal the answer</summary>

<p>The timeout only tells you the client stopped waiting. The charge may already exist. If the provider supports idempotency keys, reuse the original key for the same payment and check its recorded outcome.</p>

</details>

<!-- daily-backend:end -->
