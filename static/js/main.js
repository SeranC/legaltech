// BBG Legal Tech Assistant - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        if (!alert.classList.contains('alert-permanent')) {
            setTimeout(() => {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }, 5000);
        }
    });

    // Toast notifications
    const toasts = document.querySelectorAll('.toast');
    toasts.forEach(toast => {
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();
    });

    // Loading states for buttons
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            if (this.classList.contains('btn-loading')) {
                this.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Loading...';
                this.disabled = true;
            }
        });
    });

    // Form validation
    const forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Search functionality
    const searchInputs = document.querySelectorAll('.search-input');
    searchInputs.forEach(input => {
        input.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const searchContainer = this.closest('.search-container');
            const items = searchContainer.querySelectorAll('.search-item');

            items.forEach(item => {
                const text = item.textContent.toLowerCase();
                if (text.includes(searchTerm)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });

    // File upload preview
    const fileInputs = document.querySelectorAll('.file-input');
    fileInputs.forEach(input => {
        input.addEventListener('change', function() {
            const files = this.files;
            const preview = document.querySelector('.file-preview');

            if (preview && files.length > 0) {
                preview.innerHTML = '';
                Array.from(files).forEach(file => {
                    const fileItem = document.createElement('div');
                    fileItem.className = 'file-item d-flex align-items-center p-2 border rounded mb-2';
                    fileItem.innerHTML = `
                        <i class="bi bi-file-earmark me-2"></i>
                        <div class="flex-grow-1">
                            <small class="fw-bold">${file.name}</small>
                            <br>
                            <small class="text-muted">${(file.size / 1024).toFixed(1)} KB</small>
                        </div>
                        <button type="button" class="btn btn-sm btn-outline-danger ms-2" onclick="removeFile(this)">
                            <i class="bi bi-x"></i>
                        </button>
                    `;
                    preview.appendChild(fileItem);
                });
            }
        });
    });

    // Drag and drop file upload
    const dropZones = document.querySelectorAll('.upload-zone');
    dropZones.forEach(zone => {
        zone.addEventListener('dragover', function(e) {
            e.preventDefault();
            this.classList.add('dragover');
        });

        zone.addEventListener('dragleave', function(e) {
            e.preventDefault();
            this.classList.remove('dragover');
        });

        zone.addEventListener('drop', function(e) {
            e.preventDefault();
            this.classList.remove('dragover');

            const files = e.dataTransfer.files;
            const fileInput = this.querySelector('.file-input');

            if (fileInput && files.length > 0) {
                fileInput.files = files;
                fileInput.dispatchEvent(new Event('change'));
            }
        });
    });

    // Copy to clipboard functionality
    const copyButtons = document.querySelectorAll('.copy-btn');
    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const textToCopy = this.dataset.clipboardText || this.previousElementSibling.textContent;
            navigator.clipboard.writeText(textToCopy).then(() => {
                const originalText = this.innerHTML;
                this.innerHTML = '<i class="bi bi-check"></i> Copied!';
                this.classList.add('btn-success');
                this.classList.remove('btn-outline-secondary');

                setTimeout(() => {
                    this.innerHTML = originalText;
                    this.classList.remove('btn-success');
                    this.classList.add('btn-outline-secondary');
                }, 2000);
            });
        });
    });

    // Dynamic content loading
    const loadButtons = document.querySelectorAll('.load-more');
    loadButtons.forEach(button => {
        button.addEventListener('click', function() {
            const container = document.querySelector(this.dataset.target);
            const skeleton = document.querySelector('.skeleton-template');

            if (container && skeleton) {
                // Show loading state
                this.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Loading...';
                this.disabled = true;

                // Simulate loading delay
                setTimeout(() => {
                    const newItem = skeleton.content.cloneNode(true);
                    container.appendChild(newItem);

                    // Reset button
                    this.innerHTML = 'Load More';
                    this.disabled = false;
                }, 1000);
            }
        });
    });

    // Modal enhancements
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        modal.addEventListener('shown.bs.modal', function() {
            const focusable = this.querySelectorAll('input, button, select, textarea');
            if (focusable.length > 0) {
                focusable[0].focus();
            }
        });
    });

    // Table sorting
    const sortableHeaders = document.querySelectorAll('.sortable');
    sortableHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const table = this.closest('table');
            const tbody = table.querySelector('tbody');
            const rows = Array.from(tbody.querySelectorAll('tr'));
            const column = this.dataset.column;
            const direction = this.dataset.direction || 'asc';

            rows.sort((a, b) => {
                const aVal = a.querySelector(`[data-${column}]`).textContent;
                const bVal = b.querySelector(`[data-${column}]`).textContent;

                if (direction === 'asc') {
                    return aVal.localeCompare(bVal);
                } else {
                    return bVal.localeCompare(aVal);
                }
            });

            // Update direction
            this.dataset.direction = direction === 'asc' ? 'desc' : 'asc';
            this.querySelector('.sort-icon').className = `bi bi-chevron-${direction === 'asc' ? 'up' : 'down'} sort-icon`;

            // Reorder rows
            rows.forEach(row => tbody.appendChild(row));
        });
    });

    // Real-time search with debouncing
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    const realtimeSearch = document.querySelectorAll('.realtime-search');
    realtimeSearch.forEach(input => {
        const debouncedSearch = debounce(function() {
            // Perform search
            console.log('Searching for:', this.value);
        }, 300);

        input.addEventListener('input', debouncedSearch);
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + K for search
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            const searchInput = document.querySelector('.search-input');
            if (searchInput) {
                searchInput.focus();
            }
        }

        // Escape to close modals
        if (e.key === 'Escape') {
            const openModal = document.querySelector('.modal.show');
            if (openModal) {
                const bsModal = bootstrap.Modal.getInstance(openModal);
                if (bsModal) {
                    bsModal.hide();
                }
            }
        }
    });

    // Progress bar animations
    const progressBars = document.querySelectorAll('.progress-bar');
    progressBars.forEach(bar => {
        const targetWidth = bar.style.width;
        bar.style.width = '0%';
        setTimeout(() => {
            bar.style.width = targetWidth;
        }, 100);
    });

    // Smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Sidebar toggle functionality
    const sidebar = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebarToggle');
    const mainContent = document.querySelector('main');

    if (sidebar && sidebarToggle) {
        // Hide the toggle button
        sidebarToggle.style.display = 'none';

        // Create collapsed sidebar with icons
        const collapsedSidebar = document.createElement('div');
        collapsedSidebar.id = 'collapsed-sidebar';
        collapsedSidebar.style.cssText = `
            position: fixed;
            top: 80px;
            left: 0;
            width: 60px;
            height: calc(100vh - 80px);
            background: linear-gradient(135deg, var(--bbg-primary) 0%, var(--bbg-secondary) 100%);
            box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
            z-index: 999;
            padding: 2rem 0 1rem 0;
            border-radius: 0 15px 15px 0;
            display: block;
        `;

        // Add navigation icons to collapsed sidebar
        const navItems = [
            { icon: 'bi-files', href: '/agreement-replication' },
            { icon: 'bi-file-earmark-plus', href: '/create-agreement' },
            { icon: 'bi-chat-dots', href: '/contract-qa' },
            { icon: 'bi-table', href: '/term-sheet' },
            { icon: 'bi-graph-up', href: '/financial-analysis' },
            { icon: 'bi-book', href: '/knowledge-base' },
            { icon: 'bi-cloud-upload', href: '/upload' }
        ];

        navItems.forEach(item => {
            const iconLink = document.createElement('a');
            iconLink.href = item.href;
            iconLink.style.cssText = `
                display: block;
                text-align: center;
                padding: 0.75rem 0;
                color: rgba(255, 255, 255, 0.9) !important;
                text-decoration: none;
                transition: all 0.2s ease;
            `;
            iconLink.innerHTML = `<i class="bi ${item.icon}" style="font-size: 1.2rem;"></i>`;
            iconLink.addEventListener('mouseenter', function() {
                this.style.color = 'var(--bbg-accent)';
                this.style.backgroundColor = 'rgba(255, 255, 255, 0.1)';
            });
            iconLink.addEventListener('mouseleave', function() {
                this.style.color = 'rgba(255, 255, 255, 0.9)';
                this.style.backgroundColor = 'transparent';
            });
            collapsedSidebar.appendChild(iconLink);
        });

        document.body.appendChild(collapsedSidebar);

        // Auto-show sidebar on hover over collapsed sidebar
        let expandTimeout;
        let collapseTimeout;
        let isTransitioning = false;

        collapsedSidebar.addEventListener('mouseenter', function() {
            if (isTransitioning) return;
            clearTimeout(collapseTimeout);
            clearTimeout(expandTimeout);
            expandTimeout = setTimeout(() => {
                if (!isTransitioning) {
                    isTransitioning = true;
                    sidebar.classList.add('show');
                    mainContent.classList.add('sidebar-open');
                    collapsedSidebar.style.display = 'none';
                    setTimeout(() => { isTransitioning = false; }, 350);
                }
            }, 300);
        });

        sidebar.addEventListener('mouseenter', function() {
            clearTimeout(collapseTimeout);
            clearTimeout(expandTimeout);
        });

        // Auto-hide sidebar when mouse leaves
        const hideSidebar = () => {
            if (sidebar.classList.contains('show') && !isTransitioning) {
                clearTimeout(expandTimeout);
                collapseTimeout = setTimeout(() => {
                    if (!isTransitioning) {
                        isTransitioning = true;
                        sidebar.classList.remove('show');
                        mainContent.classList.remove('sidebar-open');
                        collapsedSidebar.style.display = 'block';
                        setTimeout(() => { isTransitioning = false; }, 350);
                    }
                }, 200);
            }
        };

        // Mouse leave events
        collapsedSidebar.addEventListener('mouseleave', hideSidebar);
        sidebar.addEventListener('mouseleave', hideSidebar);

        // Click outside to collapse
        document.addEventListener('click', function(e) {
            if (sidebar.classList.contains('show') && !isTransitioning) {
                const sidebarRect = sidebar.getBoundingClientRect();

                const isOutsideSidebar = e.clientX < sidebarRect.left || e.clientX > sidebarRect.right ||
                                       e.clientY < sidebarRect.top || e.clientY > sidebarRect.bottom;

                if (isOutsideSidebar) {
                    hideSidebar();
                }
            }
        });
    }

    console.log('BBG Legal Tech Assistant initialized');
});

// Utility functions
function removeFile(button) {
    const fileItem = button.closest('.file-item');
    if (fileItem) {
        fileItem.remove();
    }
}

function showLoading(element) {
    element.classList.add('skeleton-loader');
}

function hideLoading(element) {
    element.classList.remove('skeleton-loader');
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

// Export for use in other scripts
window.LegalTechUtils = {
    removeFile,
    showLoading,
    hideLoading,
    formatFileSize,
    formatDate,
    formatCurrency
};
