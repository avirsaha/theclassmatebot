# Database Design Documentation

## Table of Contents

1. [Overview](#overview)
2. [Tables](#tables)
   - [1. UserMaster](#usermaster)
   - [2. ClassMaster](#classmaster)
   - [3. DocumentPool](#documentpool)
   - [4. EventPool](#eventpool)
3. [Relationships](#relationships)
4. [Database Integrity](#database-integrity)
5. [Others](#others)
6. [Contact Information](#contact-information)

---

## 1. Overview <a name="overview"></a>

This project utilizes a single RDBMS MySQL database to manage various aspects of its functionality. The database comprises four key tables: `UserMaster`, `ClassMaster`, `EventPool`, and `DocumentPool`. Each table serves a specific purpose, contributing to the overall functionality and organization of the system.


## 2. Tables <a name="tables"></a>

### 1. UserMaster <a name="usermaster"></a>

The `UserMaster` table stores information about users within the system. It includes essential details such as UserID, Nickname, Password, ClassID, Role, and Badge.

| Fields     | Type      | PK | FK | Null |
|------------|-----------|----|----|------|
| `UserID`   | Large int | ✔  | -  | -    |
| `Nickname` | Varchar   | -  | -  | -    |
| `Password` | Varbinary | -  | -  | -    |
| `ClassID`  | Large int | -  | ✔ | -    |
| `Role`     | Varchar   | -  | -  | ✔    |
| `Badge`    | Varchar   | -  | -  | ✔    |

### 2. ClassMaster <a name="classmaster"></a>

The `ClassMaster` table maintains details related to classes in the system. It includes information about ClassID, Classname, Date_of_form (Date of formation), and Strength.

| Fields         | Type      | PK | FK | Null |
|----------------|-----------|----|----|------|
| `ClassID`      | Large int | ✔  | -  | -    |
| `Classname`    | Varchar   | -  | -  | -    |
| `Date_of_form` | Date      | -  | -  | -    |
| `Strength`     | Int       | -  | -  | ✔    |

### 3. DocumentPool <a name="documentpool"></a>

The `DocumentPool` table manages documents from all individual classes. It includes details such as DocID, Docname, Doc, ClassID, UserID, Tags, and Date_of_contrib.

| Fields           | Type      | PK | FK | Null |
|------------------|-----------|----|----|------|
| `DocID`          | Large int | ✔  | -  | -    |
| `Docname`        | Varchar   | -  | -  | -    |
| `Doc`            | Blob      | -  | -  | -    |
| `ClassID`        | Large int | -  | ✔  | -    |
| `UserID`         | Large int | -  | ✔  | -    |
| `Tags`           | Varchar   | -  | -  | -    |
| `Date_of_contrib`| Date      | -  | -  | -    |

### 4. EventPool <a name="eventpool"></a>

The `EventPool` table is designed to manage events from all individual classes. It includes details such as EventID, Eventname, ClassID, Date, Organizer, and Status.

| Fields      | Type      | PK | FK | Null |
|-------------|-----------|----|----|------|
| `EventID`   | Large int | ✔  | -  | -    |
| `Eventname` | Varchar   | -  | -  | -    |
| `ClassID`   | Large int | -  | ✔ | -    |
| `Date`      | Date      | -  | -  | -    |
| `Organizer` | Varchar   | -  | -  | ✔    |
| `Status`    | Bit       | -  | -  | -    |

## 3. Relationships <a name="relationships"></a>

1. **UserMaster to ClassMaster:** Many-to-One relationship, linking users to their classes.
2. **ClassMaster to DocumentPool:** One-to-Many relationship, connecting classes to their respective document(s).
3. **ClassMaster to EventPool:** One-to-Many relationship, connecting classes to their respective event(s).
4. **UserMaster to DocumentPool:** One-to-Many relationship, connecting users to their contribution(s).

## 4. Database Integrity <a name="database-integrity"></a>

Foreign key constraints are utilized to maintain referential integrity across tables, ensuring that relationships between entities are well-defined and maintained.

This database design aims to provide a robust foundation for managing users, classes, events, and documents within the context of this project, promoting effective data organization and retrieval.

## 5. Others <a name="others"></a>

For insights into the design patterns adopted in this project, please refer to the [design principles](DESIGN_PRINCIPLES.md). For detailed implementation information, consult the [implementation details](IMPL_DETAILS.md). To familiarize yourself with the coding conventions adhered to in this project, review the [style guidelines](STYLE_GUIDELINES.md). For an understanding of the privacy policy, please refer to [privacy policies](../PRIVACY_POLICY.md). Additional information can be found in the [readme](../README.md).

## 6. Contact Information <a name="contact-information"></a>

For any questions, concerns, or suggestions regarding the database design, please send us an email to aviraj.saha@outlook.com.

---

© 2023 AVIRAJ SAHA & MAITHIL SAHA. THIS OPEN-SOURCE SOFTWARE IS LICENSED UNDER THE [GPLv3.0](LICENSE).