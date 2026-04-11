---
title: "Talk: AI-Powered Database Migration That Saved $1M"
date: 2025-05-28
description: "Tech talk on leading the payment database migration from IBM DB2 to MySQL. Covered the AI-assisted conversion workflow, the custom DB Migration Quality Checker I built, the production deployment strategy, and how we handled a failed first attempt."
image: "/images/blog/tech-talk-db-migration.jpeg"
event: "Tech Talk"
company: "Bally's Interactive"
location: "London, UK"
blog_post: "/blog/migrating-payment-database-db2-to-mysql/"
tags:
  - database-migration
  - payment-systems
  - ai-tools
  - pci-compliance
---

## Event Details

| | |
|---|---|
| **Date** | 28 May 2025 |
| **Event** | Tech Talk |
| **Company** | Bally's Interactive |
| **Location** | London, UK |
| **Topic** | AI-Powered Database Migration from DB2 to MySQL |

I presented this talk at Bally's Interactive in London to share what our team went through during Project Itchy Bird. This was the migration of the payment system database from IBM DB2 to MySQL. The payment domain was the first to go through this company-wide initiative, so what we learned and the tools we built became the reference for other teams.

The audience included engineers, staff engineers, and the data operations team from across the company.

## What I Covered

- **The problem:** why the shared DB2 database was causing issues (single point of failure, PCI scope, tight coupling, high licensing costs)
- **AI-assisted conversion:** how I used Cursor AI to convert DDL and SQL queries from DB2 to MySQL, and why it worked better than manual approaches
- **Dual-database support:** the codebase architecture that let us run DB2 and MySQL side by side without blocking other work
- **The DB Migration Quality Checker:** the custom validation tool I built that compares data, schema, indexes, and metadata between databases. It runs across 109 tables in about 8 minutes and was later adopted by other teams company-wide
- **Production deployment:** the step-by-step cutover process, designed with rollback at every stage
- **The failed first attempt:** what went wrong on April 2nd, how the quality checker caught it, and how we went live successfully on April 23rd

## Impact

The migration delivered roughly $1M in annual cost savings by eliminating DB2 licensing. The tooling and approaches I developed during this project were adopted by other teams across the company for their own database migrations.

The talk itself led to direct adoption of the DB Migration Quality Checker by two other domain teams who were planning their own migrations.
