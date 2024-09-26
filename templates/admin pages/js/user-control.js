let editMode = false; // Para saber si estamos editando
let currentRow; // Fila actual que estamos editando

document.getElementById('addUserButton').addEventListener('click', function() {
    const firstName = document.getElementById('firstName').value;
    const city = document.getElementById('city').value;
    const age = document.getElementById('age').value;

    if (!firstName || !city || !age) {
        alert('Por favor, completa todos los campos.');
        return;
    }

    const today = new Date();
    const registerDate = today.toISOString().split('T')[0];

    if (editMode) {
        // Si estamos en modo de edición, actualizamos la fila existente
        currentRow.cells[0].innerText = firstName;
        currentRow.cells[1].innerText = city;
        currentRow.cells[2].innerText = age;
        editMode = false; // Salir del modo de edición
        document.getElementById('addUserButton').innerText = "Agregar Usuario"; // Cambiar el texto del botón
    } else {
        // Si no estamos en modo de edición, agregamos un nuevo usuario
        const table = document.querySelector('#dataTable tbody');
        const newRow = document.createElement('tr');

        newRow.innerHTML = `
            <td>${firstName}</td>
            <td>${city}</td>
            <td>${age}</td>
            <td>${registerDate}</td>
            <td>
                <button type="button" class="btn btn-outline-warning edit-user">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-fill" viewBox="0 0 16 16">
                        <path d="M12.854.146a.5.5 0 0 1 .146.35v2a.5.5 0 0 1-.5.5H10.5a.5.5 0 0 1-.35-.146L9 2.793 13.207.146l.146.146z"/>
                        <path fill-rule="evenodd" d="M1 13.5v2a.5.5 0 0 0 .5.5h2a.5.5 0 0 0 .354-.146L13.207 5.5l-3-3L1.5 12.793A.5.5 0 0 0 1 13.5zm3.5-.5v1H2v-1h2.5zM10 2.793l-.5-.5L2 10.793v2.5h2.5L10 4.293v-.5z"/>
                    </svg>
                    Editar Usuario
                </button>
                <button type="button" class="btn btn-outline-danger delete-user">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-dash-fill" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M11 7.5a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1h-4a.5.5 0 0 1-.5-.5"></path>
                        <path d="M1 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6"></path>
                    </svg>
                    Eliminar Usuario
                </button>
            </td>
        `;
        table.appendChild(newRow);
    }

    document.getElementById('userForm').reset();
    $('#formularioModal').modal('hide');
});

// Escucha los botones de editar
document.querySelector('#dataTable').addEventListener('click', function(event) {
    if (event.target.closest('.edit-user')) {
        const row = event.target.closest('tr');
        const firstName = row.cells[0].innerText;
        const city = row.cells[1].innerText;
        const age = row.cells[2].innerText;

        // Llenar el formulario con los datos actuales
        document.getElementById('firstName').value = firstName;
        document.getElementById('city').value = city;
        document.getElementById('age').value = age;

        // Marcar que estamos en modo de edición
        editMode = true;
        currentRow = row;
        document.getElementById('addUserButton').innerText = "Guardar Cambios"; // Cambiar el texto del botón
        $('#formularioModal').modal('show'); // Mostrar el modal
    }
});

// Delegación de eventos para eliminar usuarios
document.querySelector('#dataTable tbody').addEventListener('click', function(event) {
    if (event.target.closest('.delete-user')) {
        const row = event.target.closest('tr');
        row.remove();
    }
});
