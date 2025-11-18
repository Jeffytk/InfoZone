document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const postId = urlParams.get('post');

    const postFormContainer = document.querySelector('.nuevo-tema');

    if (postId) {
        document.getElementById('posts-view').classList.remove('active-view');
        document.getElementById('post-view').classList.add('active-view');
        displaySinglePost(postId);
        setupCommentForm(postId);

        if (postFormContainer) postFormContainer.style.display = 'none';
    } else {
        document.getElementById('posts-view').classList.add('active-view');
        document.getElementById('post-view').classList.remove('active-view');
        displayPostList();
        setupPostForm();

        if (postFormContainer) postFormContainer.style.display = 'block';
    }
});


function getPosts() {
    return JSON.parse(localStorage.getItem('saludpost')) || [];
}

function savePost(post) {
    const posts = getPosts();
    posts.unshift(post);
    localStorage.setItem('saludpost', JSON.stringify(posts));
}

function getPostById(id) {
    return getPosts().find(post => post.id === id);
}

function displayPostList() {
    const postsContainer = document.getElementById('posts-container');
    if (!postsContainer) return;

    const posts = getPosts();
    postsContainer.innerHTML = '';

    if (posts.length === 0) {
        postsContainer.innerHTML = '<p class="no-posts">No hay posts aún. ¡Sé el primero en publicar!</p>';
        return;
    }

    posts.forEach(post => {
        const postElement = document.createElement('article');
        postElement.className = 'post';
        postElement.innerHTML = `
            <h3><a href="?post=${post.id}">${post.titulo}</a></h3>
            <div class="post-meta">
                <span class="author">${post.autor}</span>
                <span class="date">${formatDate(post.fecha)}</span>
            </div>
            <div class="post-excerpt">
                <p>${post.mensaje.length > 150 ? post.mensaje.substring(0, 150) + '...' : post.mensaje}</p>
            </div>
            <a href="?post=${post.id}" class="read-more">Ver discusión completa</a>
        `;
        postsContainer.appendChild(postElement);
    });
}

function setupPostForm() {
    const form = document.getElementById('nuevoPostForm');
    if (!form) return;

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const title = document.getElementById('titulo').value.trim();
        const message = document.getElementById('mensaje').value.trim();

        if (!title || !message) {
            alert('Por favor completa todos los campos');
            return;
        }

        const newPost = {
            id: Date.now().toString(),
            titulo: title,
            mensaje: message,
            autor: 'Usuario',
            fecha: new Date().toISOString(),
            categoria: 'entretenimiento'
        };

        savePost(newPost);
        form.reset();
        displayPostList();
    });
}


function displaySinglePost(postId) {
    const post = getPostById(postId);
    if (!post) {
        window.location.href = '?';
        return;
    }

    const postContainer = document.getElementById('post-container');
    if (!postContainer) return;

    postContainer.innerHTML = `
        <article class="single-post">
            <h2>${post.titulo}</h2>
            <div class="post-meta">
                <span class="author">${post.autor}</span>
                <span class="date">${formatDate(post.fecha)}</span>
            </div>
            <div class="post-content">
                <p>${post.mensaje}</p>
            </div>
            <a href="?" class="back-link">← Volver al foro</a>
        </article>
        
        <section class="comments-section">
            <h3>Comentarios</h3>
            <div id="comments-container" class="comments-container"></div>
        </section>
    `;

    displayComments(postId);
    setupCommentForm(postId);
}


function getComments(postId) {
    const allComments = JSON.parse(localStorage.getItem('astroment')) || [];
    return allComments.filter(comment => comment.postId === postId);
}

function saveComment(comment) {
    const comments = JSON.parse(localStorage.getItem('astroment')) || [];
    comments.push(comment);
    localStorage.setItem('astroment', JSON.stringify(comments));
}

function displayComments(postId) {
    const commentsContainer = document.getElementById('comments-container');
    if (!commentsContainer) return;

    const comments = getComments(postId);
    commentsContainer.innerHTML = '';

    if (comments.length === 0) {
        commentsContainer.innerHTML = '<p class="no-comments">No hay comentarios aún. ¡Sé el primero en comentar!</p>';
        return;
    }

    comments.forEach(comment => {
        const commentElement = document.createElement('div');
        commentElement.className = 'comment';
        commentElement.innerHTML = `
            <div class="comment-meta">
                <span class="comment-author">${comment.autor}</span>
                <span class="comment-date">${formatDate(comment.fecha)}</span>
            </div>
            <div class="comment-content">
                <p>${comment.contenido}</p>
            </div>
        `;
        commentsContainer.appendChild(commentElement);
    });
}

function setupCommentForm(postId) {
    const commentsSection = document.querySelector('.comments-section');
    if (!commentsSection) return;

    if (document.getElementById('commentForm')) return;

    const commentForm = document.createElement('form');
    commentForm.id = 'commentForm';
    commentForm.className = 'comment-form';
    commentForm.innerHTML = `
        <h3>Añadir comentario</h3>
        <label for="comment-author">Nombre (opcional):</label>
        <input type="text" id="comment-author" class="comment-input">

        <label for="comment-content">Comentario:</label>
        <textarea id="comment-content" class="comment-textarea" required></textarea>

        <button type="submit" class="btn-comment">Publicar comentario</button>
    `;

    commentForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const author = document.getElementById('comment-author').value.trim() || 'Anónimo';
        const content = document.getElementById('comment-content').value.trim();

        if (!content) {
            alert('Por favor escribe un comentario');
            return;
        }

        const newComment = {
            id: Date.now().toString(),
            postId: postId,
            autor: author,
            contenido: content,
            fecha: new Date().toISOString()
        };

        saveComment(newComment);
        commentForm.reset();
        displayComments(postId);
    });

    commentsSection.appendChild(commentForm);
}


function formatDate(isoString) {
    const date = new Date(isoString);
    return date.toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

