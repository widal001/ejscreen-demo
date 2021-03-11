# Data Dictionary

This documents outlines the schema of the mapping tool's underlying datastore, organized by table.

## Indicator

Stores the unique list of indicators that are used to calculate index scores as well as metadata about those indicators, such as their original datasource, source_name, and description.


| Column      | Data Type | Example          | Notes                         |
| :---------- | :-------- |:---------------  |:----------------------------- |
| id          | integer   | 1                | Primary Key, Auto-incremented |
| category    | text      | Demographic      | May become Enum at some point |
| source      | text      | EJScreen         | May become Enum at some point |
| source_name | text      | ACSTOTPOP        | Indexed                       |
| description | text      | Total population |                               |
