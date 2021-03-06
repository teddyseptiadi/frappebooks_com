---
base_template_path: templates/doc.html
title: Getting Started with Frappe Books
intro: Let’s start applying what we have learned so far by setting up your company in Frappe Books.
related_topics:
  - title: Sales Invoice
    description: A sales invoice is a bill that you send to your customer.
    link: /docs/sales-invoice
  - title: Purchase Invoice
    description: A purchase invoice is a bill that you create when you do a purchase.
    link: /docs/purchase-invoice
  - title: Expense Voucher
    description: An expense voucher is a journal entry you do when you record an expense.
    link: /docs/expense-voucher
---

If you have not downloaded Frappe Books, this is a good time to do that. Simply
visit [frappebooks.com](https://frappebooks.com) and click on Download.

## Company Setup

When you open Frappe Books, you’ll be presented two options: New File and
Existing File. If this is the first time you are opening Frappe Books, click on
New File. Now select an appropriate location where you want to store the file
and give it a name. Usually, you would want to give the name of your company.

[screenshot]

> Frappe Books stores all your company data and transactions on a local file on
> your computer.

Now, enter your Business Name, Business Email and Country Information. This will
help set up the correct Chart of Accounts based on your country.

Congratulations! You now have a company set up on Frappe Books. You can now
start recording your invoices and transactions.

Let’s go over some simple setup steps to get you ready.

### 1. Enter bank accounts

Head over to Chart of Accounts page, by clicking on Setup > Chart of Accounts
from the sidebar. Click Assets > Current Assets > Bank Accounts.

Add any bank accounts your business has apart from the one already added. Taxes

If your company charges or will recover Sales Taxes, and add any taxes that you
will use. To access Taxes, go to:

> Setup  > Taxes

1. To add a Tax, enter a name which will make it easier to identify. You can
   also mention the rate in the name. For e.g. Service Tax - 5%.

1. Select the Tax Account and enter the Rate. You can add multiple rows with
   different Tax Accounts. This will make it easier to apply a set of Taxes
   which are frequently applied together on an Item. You can even create
   different taxes for different Items or a class of Items.

[screenshot]

### 2. Add Items

One of the most important things you will add in Books are your products or services that you provide to your customers.
To access Items,  go to:

> Sales > Items.

1. Click on the blue plus button
1. Enter the Name and Rate.
1. Select if your Item is a Product or Service. Setting the default Tax for your
   Item will fetch it automatically when you create an Invoice.

[screenshot]

### 3. Add Customers

Add your customers to record their details and select them in Invoices. You can
also import your customers in bulk if you have them in an Excel sheet.

To access Customers, go to:

> Sales > Customers

[screenshot]

### 4. Setup Opening Balances

If you are moving from an existing accounting system over to Frappe Books, you
will need to enter the account balances from your previous system.

Here are the steps to do that:

(add steps to import opening balances)

This will create a Journal Transaction in the system with all your previous
statements. This brings your books to the same position that was present in your
previous accounting system.
