# dragon-quest-V-save-editor
-Tool to decrypt Dragon Quest V Mobile save files and calculate the correct checksum.-

# - Decryption and Modification of Game Save

## Steps to Modify a Game Save

### 1. Retrieve the Save File
- Access the game files and locate the save file.
- The save file starts with `data`.
- Copy this file to an accessible location.

### 2. Decrypt the Save File
- Use the script to decrypt the file.
- Command:
  ```sh
  python save_decrypt.py decrypt data1.dat
  ```
  (Replace `data1.dat` with the exact name of your save file)

### 3. Modify the Data
- Open the decrypted file using a hex editor or a compatible text editor.
- Modify the desired values (money, levels, items, etc.).
- Save the changes.

### 4. Recalculate the Checksum
- Before re-encrypting, you need to recalculate the checksum.
- Command:
  ```sh
  python save_decrypt.py checksum data1.dat
  ```

### 5. Re-encrypt the Save File
- After modifying and recalculating the checksum, re-encrypt the file.
- Command:
  ```sh
  python save_decrypt.py encrypt data1.dat
  ```

### 6. Replace the Save File
- Replace the old save file in the game with the modified file.
- Launch the game and check if the modifications are applied.

## Command Usage

### Decrypt a Save File
```sh
python save_decrypt.py decrypt <file_name>
```

### Recalculate Checksum
```sh
python save_decrypt.py checksum <file_name>
```

### Encrypt the Save File
```sh
python save_decrypt.py encrypt <file_name>
```

## Note
- Always make a backup of your original file before making any changes.
- Using modified files may involve risks; proceed at your own discretion.
