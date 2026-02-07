#!/bin/bash

# Configure podman to use overlay2 storage driver by default

echo "Configuring podman storage driver..."

# User-level configuration
mkdir -p ~/.config/containers
cat > ~/.config/containers/storage.conf << 'EOF'
[storage]
driver = "overlay"

[storage.options.overlay]
mount_program = "/usr/bin/fuse-overlayfs"
EOF

echo "✓ User-level storage configuration created at ~/.config/containers/storage.conf"

# Optional: System-wide configuration (requires sudo)
read -p "Configure system-wide? (requires sudo) [y/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    sudo mkdir -p /etc/containers
    sudo tee /etc/containers/storage.conf > /dev/null << 'EOF'
[storage]
driver = "overlay"

[storage.options.overlay]
mount_program = "/usr/bin/fuse-overlayfs"
EOF
    echo "✓ System-wide storage configuration created at /etc/containers/storage.conf"
fi

# Create nodocker file to quiet cgroupv2 warnings
read -p "Create /etc/containers/nodocker to quiet warnings? (requires sudo) [y/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    sudo mkdir -p /etc/containers
    sudo touch /etc/containers/nodocker
    echo "✓ Created /etc/containers/nodocker"
fi

echo ""
echo "Podman configuration complete!"
echo "You can now run: podman build ."
