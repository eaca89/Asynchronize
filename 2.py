import asyncio

#  Define a coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching data ... ")
    await asyncio.sleep(delay) # Simulate an I/0 operation with a sleep
    print("Data fetched")
    return {"data": "Some data"} # Return some data

# Define another coroutine that calls the first coroutine
async def main():
    print("Start of main coroutine")
    task = fetch_data(2)
    print("End of main coroutine")

    result = await task
    print(f"Received result: {result}")

# Run the main coroutine
asyncio.run(main())
