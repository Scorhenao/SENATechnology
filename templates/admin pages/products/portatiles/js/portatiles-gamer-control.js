// Obtiene las laptops guardadas en localStorage (si existen)
let laptops = JSON.parse(localStorage.getItem('laptops')) || [];

// Función para guardar laptops en localStorage
function saveToLocalStorage() {
    localStorage.setItem('laptops', JSON.stringify(laptops));
}

// Función para renderizar laptops
function renderLaptops() {
    const laptopsSection = document.getElementById('laptopsSection');
    laptopsSection.innerHTML = ''; // Limpia la sección antes de renderizar nuevamente

    laptops.forEach((laptop, index) => {
        const card = document.createElement('div');
        card.classList.add('card');
        card.style.width = '18rem';

        card.innerHTML = `
            <img src="${laptop.image}" class="card-img-top" alt="${laptop.title}">
            <div class="card-body">
                <h5 class="card-title">${laptop.title}</h5>
                <p class="card-text">${laptop.description}</p>
            </div>
            <ul class="list-group list-group-flush">
                ${laptop.specs.map(spec => `<li class="list-group-item">${spec}</li>`).join('')}
            </ul>
            <div class="card-body">
                <button class="btn btn-primary" onclick="openViewMoreModal(${index})">Ver más</button>
                <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#laptopModal" onclick="editLaptop(${index})">Editar</button>
                <button class="btn btn-danger" onclick="deleteLaptop(${index})">Eliminar</button>
            </div>
        `;

        laptopsSection.appendChild(card);
    });
}

// Función para añadir o actualizar laptop
document.getElementById('saveLaptopBtn').addEventListener('click', function() {
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const specs = document.getElementById('specs').value.split(',').map(spec => spec.trim());
    const image = document.getElementById('image').value;
    const index = document.getElementById('laptopIndex').value;

    const laptopData = { title, description, specs, image };

    if (index === "") {
        // Crear nueva laptop
        laptops.push(laptopData);
    } else {
        // Editar laptop existente
        laptops[index] = laptopData;
        document.getElementById('laptopIndex').value = "";
    }

    // Guardar en localStorage
    saveToLocalStorage();

    // Resetear formulario
    document.getElementById('laptopForm').reset();

    // Cerrar el modal
    const modal = bootstrap.Modal.getInstance(document.getElementById('laptopModal'));
    modal.hide();

    // Renderizar las laptops nuevamente
    renderLaptops();
});

// Función para editar laptop
function editLaptop(index) {
    const laptop = laptops[index];

    document.getElementById('title').value = laptop.title;
    document.getElementById('description').value = laptop.description;
    document.getElementById('specs').value = laptop.specs.join(', ');
    document.getElementById('image').value = laptop.image;
    document.getElementById('laptopIndex').value = index;
}

// Función para eliminar laptop
function deleteLaptop(index) {
    // Elimina la laptop del array de laptops usando splice
    laptops.splice(index, 1);

    // Guardar el cambio en localStorage
    saveToLocalStorage();

    // Vuelve a renderizar las laptops para reflejar los cambios
    renderLaptops();
}

// Función para abrir el modal con los detalles de la laptop
function openViewMoreModal(index) {
    const laptop = laptops[index]; // Obtener los detalles de la laptop

    // Asignar los detalles de la laptop al modal
    document.getElementById('modalLaptopImage').src = laptop.image;
    document.getElementById('modalLaptopTitle').textContent = laptop.title;
    document.getElementById('modalLaptopDescription').textContent = laptop.description;
    
    // Limpiar y añadir especificaciones
    const specsList = document.getElementById('modalLaptopSpecs');
    specsList.innerHTML = ''; // Limpiar la lista
    laptop.specs.forEach(spec => {
        const li = document.createElement('li');
        li.classList.add('list-group-item');
        li.textContent = spec;
        specsList.appendChild(li);
    });

    // Mostrar el modal
    const modal = new bootstrap.Modal(document.getElementById('viewMoreModal'));
    modal.show();
}

// Renderizar laptops al cargar la página
renderLaptops();
