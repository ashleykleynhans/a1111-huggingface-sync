#!/usr/bin/env python3
import os
import argparse
from huggingface_hub import HfApi


def get_args():
    parser = argparse.ArgumentParser(
        description='Upload a file to Huggingface',
    )

    parser.add_argument(
        'file',
        type=str,
        help='filename'
    )

    parser.add_argument(
        'dest',
        type=str,
        help='Huggingface dest path'
    )

    parser.add_argument(
        'repo_id',
        type=str,
        help='Huggingface repo_id'
    )

    return parser.parse_args()


if __name__ == '__main__':
    if not os.getenv('HF_TOKEN'):
        raise Exception('HF_TOKEN environment variable is not set')

    args = get_args()
    api = HfApi()

    uri = api.upload_file(
        path_or_fileobj=args.file,
        path_in_repo=args.dest,
        repo_id=args.repo_id
    )

    if uri:
        print(f'{args.file} was uploaded successfully: {uri}')

