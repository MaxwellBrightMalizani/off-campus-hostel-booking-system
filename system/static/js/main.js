// Main JavaScript file with interactive features
console.log('Main.js loaded - Interactive Mode');

// Smooth scroll behavior and intersection observer animations
document.addEventListener('DOMContentLoaded', function() {
  // Animate elements on scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Observe all property cards and feature cards
  document.querySelectorAll('.property-card, .feature-card, .dash-card').forEach(el => {
    el.style.opacity = '0';
    observer.observe(el);
  });

  // Add button ripple effect
  document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', function(e) {
      const ripple = document.createElement('span');
      const rect = this.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);
      const x = e.clientX - rect.left - size / 2;
      const y = e.clientY - rect.top - size / 2;
      
      ripple.style.width = ripple.style.height = size + 'px';
      ripple.style.left = x + 'px';
      ripple.style.top = y + 'px';
      ripple.classList.add('ripple');
      
      this.appendChild(ripple);
      setTimeout(() => ripple.remove(), 600);
    });
  });

  // Add nav link active state tracking
  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach(link => {
    link.addEventListener('click', function() {
      navLinks.forEach(l => l.classList.remove('active-nav'));
      this.classList.add('active-nav');
    });
  });

  // Form input focus effects
  document.querySelectorAll('.form-control').forEach(input => {
    input.addEventListener('focus', function() {
      this.parentElement.style.transform = 'scale(1.02)';
      this.parentElement.style.transition = 'transform 0.2s';
    });
    input.addEventListener('blur', function() {
      this.parentElement.style.transform = 'scale(1)';
    });
  });

  // Scroll animation for hero section
  window.addEventListener('scroll', function() {
    const hero = document.querySelector('.hero-section');
    if (hero) {
      const scrolled = window.pageYOffset;
      const parallax = scrolled * 0.5;
      hero.style.backgroundPosition = `0 ${parallax}px`;
    }
  });

  // Number counter animation
  animateCounters();

  // Search form enhancement
  const searchForm = document.querySelector('.search-box form');
  if (searchForm) {
    searchForm.addEventListener('submit', function() {
      const btn = this.querySelector('button');
      btn.disabled = true;
      btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Searching...';
    });
  }

  const themeToggle = document.getElementById('darkModeToggle');
  if (themeToggle) {
    const savedTheme = localStorage.getItem('theme');
    const darkMode = savedTheme === 'dark';
    setTheme(darkMode);

    themeToggle.addEventListener('click', function(e) {
      e.preventDefault();
      const isDark = document.body.classList.toggle('dark-mode');
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
      setTheme(isDark);
    });

  }
});

function setTheme(isDark) {
  document.body.classList.toggle('dark-mode', isDark);
  const themeToggle = document.getElementById('darkModeToggle');
  if (themeToggle) {
    themeToggle.setAttribute('aria-pressed', isDark ? 'true' : 'false');
    themeToggle.classList.toggle('is-dark', isDark);
  }
}

// Animate number counters
function animateCounters() {
  const counters = document.querySelectorAll('.stat-num');
  counters.forEach(counter => {
    const target = parseInt(counter.textContent);
    if (isNaN(target)) return;
    
    let current = 0;
    const increment = target / 30;
    const timer = setInterval(() => {
      current += increment;
      if (current >= target) {
        counter.textContent = target;
        clearInterval(timer);
      } else {
        counter.textContent = Math.ceil(current);
      }
    }, 50);
  });
}

// Add ripple effect styles
const style = document.createElement('style');
style.textContent = `
  .ripple {
    position: absolute;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.6);
    transform: scale(0);
    animation: ripple-animation 0.6s ease-out;
    pointer-events: none;
  }

  @keyframes ripple-animation {
    to {
      transform: scale(4);
      opacity: 0;
    }
  }

  .form-control:focus {
    border-color: #198754 !important;
    box-shadow: 0 0 0 0.2rem rgba(25, 135, 84, 0.15) !important;
  }
`;
document.head.appendChild(style);
