#!/bin/bash

total_size=0
declare -A status_codes

print_metrics() {
    echo "Total file size: $total_size"
    for code in $(echo "${!status_codes[@]}" | tr ' ' '\n' | sort -n); do
        echo "$code: ${status_codes[$code]}"
    done
}

process_line() {
    line=$1
    parts=($line)

    if [ "${#parts[@]}" -lt 9 ]; then
        return
    fi

    ip_address=${parts[0]}
    date=${parts[3]:1}
    status_code=${parts[${#parts[@]}-2]}
    file_size=${parts[${#parts[@]}-1]}

    # Update total file size
    total_size=$((total_size + file_size))

    # Update status code count
    if [[ $status_code =~ ^[0-9]+$ ]]; then
        ((status_codes[$status_code]++))
    fi
}

lines_processed=0

trap 'print_metrics' SIGINT

while read -r line; do
    process_line "$line"
    lines_processed=$((lines_processed + 1))

    if [ $((lines_processed % 10)) -eq 0 ]; then
        print_metrics
    fi
done

print_metrics
