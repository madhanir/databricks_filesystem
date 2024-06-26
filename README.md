Introduction
---
Databricks stands out as a leading service for big data processing, yet it lacks support for several essential file system operations commonly needed by developers. Consequently, developers often have to craft custom solutions to fill this gap. The missing operations include:

- Recursively listing directory contents
- Listing files matching specified start and end patterns
- Performing case-sensitive or case-insensitive file pattern matches
- Listing only directories or only files or both
- Generating sorted output of listing

Fortunately, with the availability of this package, you can effortlessly execute these operations.

Package installation and configuration
---
1. Install the package using the pip command
```
pip install databricks-filesystem
```
2. Import the package
```
from databricks_filesystem import DatabricksFilesystem
```
3. Configure the package by passing the databricks Utils (dbutils) as a parameter
```
adb_fs = DatabricksFilesystem(dbutils=dbutils)
```
4. Execute the `filesystem_list` function of the package to recursively list files and directories. Below are examples demonstrating its compatibility with DBFS and various external storage systems such as Azure Data Lake Storage (ADLS), Azure Blob Storage, AWS S3, Google Storage, and more.
```
# List DBFS directory
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/")

# List Azure Data Lake Storage directory (ADLS)
adb_fs.filesystem_list(filesystem_path="abfss://<container>@<storage-account>.dfs.core.windows.net/<directory>/")

# List AWS S3
adb_fs.filesystem_list(filesystem_path="s3a://<aws-bucket-name>/<path>")

# List Google Storage
adb_fs.filesystem_list(filesystem_path="gs://<bucket-name>/<path>")
```
filesystem_list function
---
```
filesystem_list(self, filesystem_path: str, recursive_flag: bool = True, list_directories: bool = True, list_files: bool = True, files_starts_with: Union[str, List[str]] = None, files_ends_with: Union[str, List[str]] = None, skip_files_starts_with: Union[str, List[str]] = None, skip_files_ends_with: Union[str, List[str]] = None, case_sensitive_comparison: bool = True, sorted_output: bool = True) -> list
```

Below are the parameters accepted by the `filesystem_list` function:
-  filesystem_path (str - Mandatory): Specify the file system path for listing.

- recursive_flag (bool - Optional (Default: True)): When set to True, this flag enables recursive listing of the file system path, including all subdirectories.

- list_directories (bool - Optional (Default: True)): When set to True, this determines whether directories will be included in the output. If enabled, directories will be listed in the output.

- list_files (bool - Optional (Default: True)): When set to True, this determines whether files will be included in the output. If enabled, files will be listed in the output.

- files_starts_with (str or List[str] - Optional (Default: None)): The provided pattern or list of patterns dictates that only files starting with it will be listed in the output. This parameter operates exclusively when the "list_files" parameter is set to True, ensuring selective listing based on the specified pattern or list of patterns.

- files_ends_with (str or List[str] - Optional (Default: None)): The provided pattern or list of patterns dictates that only files ending with it will be listed in the output. This parameter operates exclusively when the "list_files" parameter is set to True, ensuring selective listing based on the specified pattern or list of patterns.

- skip_files_starts_with (str or List[str] - Optional (Default: None)): The provided pattern or list of patterns dictates that files starting with it will be excluded in the output. This parameter operates exclusively when the "list_files" parameter is set to True, ensuring selective listing based on the specified pattern or list of patterns.

- skip_files_ends_with (str or List[str] - Optional (Default: None)): The provided pattern or list of patterns dictates that files ending with it will be excluded in the output. This parameter operates exclusively when the "list_files" parameter is set to True, ensuring selective listing based on the specified pattern or list of patterns.

- case_sensitive_comparison (bool - Optional (Default: True)): When set to True, this parameter determines whether case-sensitive comparison will be applied for file pattern matching. It only functions when the "list_files" parameter is True and values are provided for "files_starts_with", "files_ends_with", "skip_files_starts_with", or "skip_files_ends_with".

- sorted_output (bool - Optional (Default: True)): When set to True, this parameter determines whether the output will be sorted. If enabled, the output will be returned in a sorted manner, facilitating easier navigation and analysis of the results.

The function returns the list of file paths and directory paths.

Examples
---
1. Recursively listing
```
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/")
```

2. Non-recurisve listing
```
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/", recursive_flag=False)
```

3. Recursively list only files
```
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/", list_directories=False)
```

4. Recursively list only directories
```
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/", list_files=False)
```

5. List all CSV files recursively
```
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/", list_directories=False, files_ends_with=".csv")
```

6. List all CSV, Parquet, and JSON files recursively
```
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/", list_directories=False, files_ends_with=[".csv", ".parquet", ".json"])
```

7. Recursively list all files that start with the word "test"
```
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/", list_directories=False, files_starts_with="test")
```

8. Recursively list all files that start with the word "test" or "temp"
```
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/", list_directories=False, files_starts_with=["test", "temp"])
```

9. Recursively list files that start with "part" and end with ".parquet"
```
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/", list_directories=False, files_starts_with="part", files_ends_with=".parquet")
```

10. Recursively list files that start with "part" or "test" and end with ".parquet" or ".json"
```
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/", list_directories=False, files_starts_with=["part", "test"], files_ends_with=[".parquet", ".json"])
```

11. Recursively list files, but skip those with a ".json" or ".parquet" extension
```
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/", list_directories=False, skip_files_ends_with=[".json", ".parquet"])
```

12. Recursively list files, but skip those starting with "test" or "temp" and also skip ".crc" files
```
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/", list_directories=False, skip_files_starts_with=["test", "temp"], skip_files_ends_with=[".crc"])
```

13. Perform above file pattern match case-insensitively
```
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/", list_directories=False, files_starts_with="part", files_ends_with=".parquet", case_sensitive_comparison=False)
```

14. Get the non-sorted output of the listing
```
adb_fs.filesystem_list(filesystem_path="dbfs:/FileStore/", sorted_output=False)
```

Additional Information
---
You can get more information about this package [here](https://medium.com/data-engineer-things/finally-in-databricks-we-can-now-perform-recursive-directory-listing-and-many-more-operations-c5f32aad78e7)
