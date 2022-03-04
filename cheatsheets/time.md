Format specifiers for time on a UNIX / linux system
===================================================


| Specifier    | Description                       | Example                 |
|--------------|-----------------------------------|-------------------------|
| %%           | A % character                     | %                       |
| %a           | Abbreviated weekday name          | Tue                     |
| %A           | Full weekday name                 | Tuesday                 |
| %b, %h       | Abbreviated month name            | Feb                     |
| %B           | Full month name                   | February                |
| %c           | Date and time                     | Tue Feb 1 21:39:46 2011 |
| %d           | Day of month (2 digits, 01 to 31) | 01                      |
| %D           | American date (same as %m/%d/%y)  | 02/01/11                |
| %e           | Day of month (2 chars)            | 1                       |
| %F           | ISO date (same as %Y-%m-%d)       | 2011-02-01              |
| %H           | Hour (24-hour clock, 2 digits)    | 21                      |
| %I           | Hour (12-hour clock, 2 digits)    | 09                      |
| %j           | Day of year (3 digits, 001 to 366)| 032                     |
| %m           | Decimal month (2 digits, 01 to 12)| 02                      |
| %M           | Minute (2 digits)                 | 39                      |
| %p           | AM/PM                             | PM                      |
| %P           | am/pm (GNU extension)             | pm                      |
| %R           | 24-hour time (same as %H:%M)      | 21:39                   |
| %S           | SEcond (00 to 60)                 | 37                      |
| %T           | Time (same as %H:%M%:S)           | 16:24:02                |
| %u           | weeday number (1 to 7, Monday = 1)| 2                       |
| %U           | Sundaay week number (00 to 53)    | 05                      |
| %w           | Weekday number (0 to 6, Sunday=0) | 2                       |
| %W           | MOnday week number (00 to 53)     | 05                      |
| %x           | Date (localized)                  | 02/01/11                |
| %X           | Time (localized)                  | 21:39:46                |
| %Y           | 4-digit year                      | 2011                    |
| %Z           | Timezone name                     | CET                     |
