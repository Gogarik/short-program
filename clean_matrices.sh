#!/bin/bash

TARGET_DIR="random_matrices"

if [ -d "$TARGET_DIR" ]; then
    rm -rf "$TARGET_DIR"/*
    echo "Все файлы из папки $TARGET_DIR удалены."
else
    echo "Ошибка: Папка $TARGET_DIR не существует."
fi
