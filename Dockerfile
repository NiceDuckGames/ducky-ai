# Use a Rust base image
FROM rust:1.71 as builder

WORKDIR /usr/src/

# Copy the application source code
COPY . .

# Build the Rust application
RUN cargo build --release

# Final lightweight image
FROM debian:buster-slim

WORKDIR /usr/src/app

# Copy the built binary from the builder stage
COPY --from=builder /usr/src/target/release/duckyai .

# Start the Rust application
CMD ["./duckyai"]
