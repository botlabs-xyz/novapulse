(() => {
  const navToggle = document.querySelector('.nav-toggle');
  const primaryNav = document.querySelector('.primary-nav');

  if (navToggle && primaryNav) {
    const closeNav = () => {
      primaryNav.classList.remove('is-open');
      navToggle.setAttribute('aria-expanded', 'false');
    };

    navToggle.addEventListener('click', () => {
      const open = !primaryNav.classList.contains('is-open');
      primaryNav.classList.toggle('is-open', open);
      navToggle.setAttribute('aria-expanded', String(open));
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') closeNav();
    });
  }

  document.querySelectorAll('pre').forEach((pre) => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'copy-button';
    button.textContent = 'Copy';
    button.setAttribute('aria-label', 'Copy command example');
    button.addEventListener('click', async () => {
      try {
        const source = pre.querySelector('code');
        await navigator.clipboard.writeText(source ? source.innerText : pre.textContent);
        button.textContent = 'Copied';
        window.setTimeout(() => { button.textContent = 'Copy'; }, 1600);
      } catch {
        button.textContent = 'Select text';
      }
    });
    pre.appendChild(button);
  });

  const search = document.querySelector('#docs-search');
  const results = document.querySelector('#search-results');
  let searchIndex = [];

  if (search && results) {
    const baseurl = document.documentElement.dataset.baseurl || '';
    fetch(`${baseurl}/search.json`)
      .then((response) => response.json())
      .then((data) => { searchIndex = data; })
      .catch(() => { searchIndex = []; });

    search.addEventListener('input', () => {
      const query = search.value.trim().toLowerCase();
      results.replaceChildren();
      if (query.length < 2) {
        results.hidden = true;
        return;
      }

      const matches = searchIndex.filter((item) =>
        `${item.title} ${item.description} ${item.section || ''}`.toLowerCase().includes(query)
      ).slice(0, 8);

      if (!matches.length) {
        const empty = document.createElement('p');
        empty.textContent = 'No matching documentation found.';
        empty.style.padding = '0 0.8rem';
        results.appendChild(empty);
      } else {
        matches.forEach((item) => {
          const link = document.createElement('a');
          link.href = item.url;
          const title = document.createElement('strong');
          title.textContent = item.title;
          const description = document.createElement('small');
          description.textContent = item.description;
          link.append(title, description);
          results.appendChild(link);
        });
      }
      results.hidden = false;
    });

    document.addEventListener('click', (event) => {
      if (!results.contains(event.target) && event.target !== search) results.hidden = true;
    });
  }

  const sidebarToggle = document.querySelector('.sidebar-toggle');
  const sectionNavigation = document.querySelector('#section-navigation');
  if (sidebarToggle && sectionNavigation) {
    sidebarToggle.addEventListener('click', () => {
      const open = !sectionNavigation.classList.contains('is-open');
      sectionNavigation.classList.toggle('is-open', open);
      sidebarToggle.setAttribute('aria-expanded', String(open));
    });
  }

  const pagination = document.querySelector('[data-page-pagination]');
  const sidebarLinks = [...document.querySelectorAll('.docs-sidebar nav a')];
  if (pagination && sidebarLinks.length) {
    const currentPath = window.location.pathname.replace(/index\.html$/, '');
    const currentIndex = sidebarLinks.findIndex((link) =>
      new URL(link.href).pathname.replace(/index\.html$/, '') === currentPath
    );
    const addPageLink = (link, label) => {
      if (!link) return;
      const clone = document.createElement('a');
      clone.href = link.href;
      const small = document.createElement('small');
      small.textContent = label;
      clone.append(small, document.createTextNode(link.textContent.trim()));
      pagination.appendChild(clone);
    };
    addPageLink(sidebarLinks[currentIndex - 1], 'Previous');
    addPageLink(sidebarLinks[currentIndex + 1], 'Next');
  }

  const backToTop = document.querySelector('.back-to-top');
  if (backToTop) {
    const updateBackToTop = () => { backToTop.hidden = window.scrollY < 520; };
    window.addEventListener('scroll', updateBackToTop, { passive: true });
    backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    updateBackToTop();
  }
})();
