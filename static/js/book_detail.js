document.addEventListener('DOMContentLoaded', function() {
    // Add to cart animation
    const addToCartBtn = document.querySelector('.add-to-cart');
    addToCartBtn.addEventListener('click', function() {
        this.classList.add('btn-success');
        this.textContent = 'Added to Cart';
        setTimeout(() => {
            this.classList.remove('btn-success');
            this.textContent = 'Add to Cart';
        }, 2000);
    });

    // Add to wishlist animation
    const addToWishlistBtn = document.querySelector('.add-to-wishlist');
    addToWishlistBtn.addEventListener('click', function() {
        this.classList.add('btn-danger');
        this.textContent = 'Added to Wishlist';
        setTimeout(() => {
            this.classList.remove('btn-danger');
            this.textContent = 'Add to Wishlist';
        }, 2000);
    });

    // Review form submission animation
    const reviewForm = document.getElementById('new-review-form');
    reviewForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const submitBtn = this.querySelector('button[type="submit"]');
        submitBtn.textContent = 'Submitting...';
        submitBtn.disabled = true;
        setTimeout(() => {
            submitBtn.textContent = 'Submitted!';
            submitBtn.classList.add('btn-success');
            setTimeout(() => {
                submitBtn.textContent = 'Submit Review';
                submitBtn.classList.remove('btn-success');
                submitBtn.disabled = false;
                this.reset();
            }, 2000);
        }, 1000);
    });

    // Related books hover animation
    const relatedBooks = document.querySelectorAll('#related-books .card');
    relatedBooks.forEach(book => {
        book.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        book.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});
