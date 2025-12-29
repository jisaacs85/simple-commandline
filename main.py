import argparse

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(
        description='A simple greeter program',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --name Alice
  python main.py --name Bob --greeting Hello --count 3
        """
    )

    # Add arguments
    parser.add_argument(
        '--name', '-n',
        type=str,
        required=True,
        help='Name of the person to greet'
    )

    parser.add_argument(
        '--greeting', '-g',
        type=str,
        default='Hi',
        help='Greeting message (default: Hi)'
    )

    parser.add_argument(
        '--count', '-c',
        type=int,
        default=1,
        help='Number of times to repeat greeting (default: 1)'
    )

    parser.add_argument(
        '--uppercase', '-u',
        action='store_true',
        help='Convert output to uppercase'
    )

    # Parse arguments
    args = parser.parse_args()

    # Build greeting message
    message = f"{args.greeting}, {args.name}!"

    if args.uppercase:
        message = message.upper()

    # Print greeting
    for i in range(args.count):
        print(f"{i + 1}. {message}")


if __name__ == '__main__':
    main()